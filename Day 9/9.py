def process(file):
    f = open(file, "r")
    strings = f.read().split()
    f.close()

    return strings

def grid(input):
    strings = process(input)
    matrix =[]
    toprow = "".join(["9" for x in range(len(strings[0]) + 2)])
    matrix.append(toprow)

    for i in strings:
        matrix.append("9" + i + "9")

    botrow = "".join(["9" for x in range(len(strings[0]) + 2)])
    matrix.append(botrow)

    return matrix

def low_points(input):
    matrix = grid(input)
    points = []

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] != "9":
                if int(matrix[i][j]) < int(matrix[i+1][j]) and int(matrix[i][j]) < int(matrix[i-1][j]) and int(matrix[i][j]) < int(matrix[i][j+1]) and int(matrix[i][j]) < int(matrix[i][j-1]):
                    points.append([matrix[i][j], i, j])

    return points

def sumup(input):
    lows = low_points(input)
    points = [int(x[0]) for x in lows]
    puzzle1_sum = sum(points) + len(points)

    return puzzle1_sum

def next_point(matrix, i, j, coords_list):
    coords_list.append([i, j])

    if matrix[i+1][j] != "9" and [i+1, j] not in coords_list:
        next_point(matrix, i+1, j, coords_list)

    if matrix[i-1][j] != "9" and [i-1, j] not in coords_list:
        next_point(matrix, i-1, j, coords_list)

    if matrix[i][j+1] != "9" and [i, j+1] not in coords_list:
        next_point(matrix, i, j+1, coords_list)

    if matrix[i][j-1] != "9" and [i, j-1] not in coords_list:
        next_point(matrix, i, j-1, coords_list)

def find_basin(input, coords):
    coords_list = []
    matrix = grid(input)
    i, j = coords[1], coords[2]
    next_point(matrix, i, j, coords_list)

    return coords_list

def basins(input):
    points = low_points(input)
    basin_list = []

    for i in points:
        basin_list.append(find_basin(input, i))
    
    return basin_list

def basin_product(input):
    basin = basins(input)
    size = [len(x) for x in basin]
    sorted_size = sorted(size, reverse=True)
    big_three = [sorted_size[0], sorted_size[1], sorted_size[2]]
    product = 1

    for i in big_three:
        product = product * i

    return product

def main():
    puzzle_input = "9.txt"
    solved1 = sumup(puzzle_input)
    solved2 = basin_product(puzzle_input)

    print(f"For Puzzle 1: {solved1}")
    print(f"For Puzzle 2: {solved2}")

if __name__ == "__main__":
    main()