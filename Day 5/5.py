from copy import deepcopy

def process_file(textfile):
    f = open(textfile, "r")
    lines_list = f.read().split("\n")
    f.close()

    return lines_list

def coords(line):
    a, b = line.split(" -> ")
    x1, y1 = a.split(",")
    x2, y2 = b.split(",")

    return x1, y1, x2, y2

def x_y_value(line):
    a, b, c, d = coords(line)
    x1, y1, x2, y2 = int(a), int(b), int(c), int(d)

    if x1 == x2:
        return "x", x1

    if y1 == y2:
        return "y", y1

    if abs(x2 - x1) == abs(y2 - y1):
        if x2 - x1 > 0 and y2 - y1 > 0:
            return "diag", 1

        if x2 - x1 < 0 and y2 - y1 > 0:
            return "diag", 2

        if x2 - x1 < 0 and y2 - y1 < 0:
            return "diag", 3

        if x2 - x1 > 0 and y2 - y1 < 0:
            return "diag", 4
    
    return False

def vert_hori_filter(lines_list):
    lines = [x for x in lines_list if x_y_value(x) != False]
    vert_hori = [x for x in lines if x_y_value(x)[0] != "diag"]

    return vert_hori

def filter(lines_list):
    lines = [x for x in lines_list if x_y_value(x) != False]

    return lines

def grid_generator(x_values, y_values):
    grid = [[0 for _ in range(x_values)] for _ in range(y_values)]

    return grid

def ploter(raw, lines):
    grid = deepcopy(raw)

    for i in lines:
        a, b, c, d = coords(i)
        xy, value = x_y_value(i)
        x1, y1, x2, y2 = int(a), int(b), int(c), int(d)

        if xy == "x":
            if y1 > y2:
                for j in range(y2, y1+1):
                    grid[j][value] += 1
            
            if y2 > y1:
                for j in range(y1, y2+1):
                    grid[j][value] += 1

        if xy == "y":
            if x1 > x2:
                for j in range(x2, x1+1):
                    grid[value][j] += 1
            
            if x2 > x1:
                for j in range(x1, x2+1):
                    grid[value][j] += 1

        if xy == "diag":
            if value == 1:
                for i in range(x2 - x1 + 1):
                    grid[y1 + i][x1 + i] += 1

            if value == 2:
                for i in range(x1 - x2 + 1):
                    grid[y1 + i][x1 - i] += 1
                
            if value == 3:
                for i in range(x1 - x2 + 1):
                    grid[y1 - i][x1 - i] += 1
                
            if value == 4:
                for i in range(x2 - x1 + 1):
                    grid[y1 - i][x1 + i] += 1    

    return grid

def intersections(grid):
    count = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] != 0 and grid[i][j] != 1:
                count += 1

    return count

def main():
    lines = process_file("5.txt")
    grid = grid_generator(1000, 1000)

    vert_hori = vert_hori_filter(lines)
    diag = filter(lines)
    final1 = ploter(grid, vert_hori)
    final2 = ploter(grid, diag)
    count1 = intersections(final1)
    count2 = intersections(final2)

    print(f"For Puzzle 1: {count1}")
    print(f"For Puzzle 2: {count2}")

if __name__ == "__main__":
    main()