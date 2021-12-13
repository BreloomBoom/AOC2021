def process(inputs):
    f = open(inputs, "r")
    a, b = f.read().split("\n\n")
    f.close()

    points = []
    for i in a.split():
        points.append(i.split(","))

    folds = []
    for i in b.split("\n"):
        folds.append(i.split(" ")[2].split("="))

    return points, folds

def folding(points, fold):
    new_points = []

    if fold[0] == "x":
        for i in points:
            a, b = int(i[0]), int(fold[1])

            if a > b:
                new_x = 2 * b - a
                point = [str(new_x), i[1]]
                
                if point not in new_points:
                    new_points.append(point)

            else:
                if i not in new_points:
                    new_points.append(i)

    if fold[0] == "y":
        for i in points:
            a, b = int(i[1]), int(fold[1])

            if a > b:
                new_y = 2 * b - a
                point = [i[0], str(new_y)]
                
                if point not in new_points:
                    new_points.append(point)

            else:
                if i not in new_points:
                    new_points.append(i)

    return new_points

def folder1(inputs):
    points, folds = process(inputs)
    points = folding(points, folds[0])

    return points

def folder2(inputs):
    points, folds = process(inputs)

    for i in folds:
        points = folding(points, i)

    return points

def to_matrix(inputs):
    max_x = 0
    max_y = 0
    points = folder2(inputs)

    for i in points:
        x, y = int(i[0]), int(i[1])

        if x > max_x:
            max_x = x

        if y > max_y:
            max_y = y

    matrix = [[" " for i in range(max_x+1)] for j in range(max_y+1)]

    return matrix

def plot(inputs):
    points = folder2(inputs)
    matrix = to_matrix(inputs)

    for i in points:
        x, y = int(i[0]), int(i[1])
        matrix[y][x] = "█"

    return matrix

def stitch(inputs):
    matrix = plot(inputs)

    for i in range(len(matrix)):
        matrix[i] = "".join(matrix[i])

    final = "\n".join(matrix)

    return final
    
def main():
    inputs = "13.txt"

    solution1 = len(folder1(inputs))
    solution2 = stitch(inputs)

    print(f"For Puzzle 1: {solution1}")
    print(f"For Puzzle 2: \n{solution2}")

if __name__ == "__main__":
    main()