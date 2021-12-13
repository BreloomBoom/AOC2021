def process(file):
    f = open(file, "r")
    strings = f.read().split()
    f.close()

    return strings

def edges(inputs):
    paths = process(inputs)
    first = []
    second = []

    for i in paths:
        a, b = i.split("-")

        if a not in first:
            first.append(a)

        placea = first.index(a)

        if len(first) != len(second):
            second.append([b])

        else:
            second[placea].append(b)

        if b not in first:
            first.append(b)

        placeb = first.index(b)

        if len(first) != len(second):
            second.append([a])

        else:
            second[placeb].append(a)

    return first, second

def dfs(edge, point, path, paths, small):
    first, second = edge
    index = first.index(point)
    next_node = second[index]

    if point == "end":
        paths.append(path)

    for i in next_node:
        if i not in small:
            if i == i.lower():
                dfs(edge, i, path+[i], paths, small+[i])

            else:
                dfs(edge, i, path+[i], paths, small)

def paths_found(inputs):
    edge = edges(inputs)
    paths = []
    dfs(edge, "start", ["start"], paths, ["start"])

    return paths

def dfs2(edge, point, path, paths, small, again):
    first, second = edge
    index = first.index(point)
    next_node = second[index]

    if point == "end":
        if path not in paths:
            paths.append(path)
            print(path)

    for i in next_node:
        if i not in small:
            if again == False:
                if i == i.lower() and i != "end":
                    dfs2(edge, i, path+[i], paths, small, True)

                    dfs2(edge, i, path+[i], paths, small+[i], False)

                elif i == "end":
                    dfs2(edge, i, path+[i], paths, small+[i], False)
                    
                else:
                    dfs2(edge, i, path+[i], paths, small, False)

            else:
                if i == i.lower():
                    dfs2(edge, i, path+[i], paths, small+[i], True)

                else:
                    dfs2(edge, i, path+[i], paths, small, True)

def paths_found2(inputs):
    edge = edges(inputs)
    paths = []
    dfs2(edge, "start", ["start"], paths, ["start"], False)

    return paths

def main():
    puzzle_input = "12.txt"

    solution1 = len(paths_found(puzzle_input))
    solution2 = len(paths_found2(puzzle_input))

    print(f"For Puzzle 1: {solution1}")
    print(f"For Puzzle 2: {solution2}")

if __name__ == "__main__":
    main()