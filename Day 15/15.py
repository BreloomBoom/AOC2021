def process(file):
    f = open(file, "r")
    strings = f.read().split()
    f.close()

    return strings

def grid(input):
    strings = process(input)
    matrix =[]
    toprow = [9 for _ in range(len(strings[0]) + 2)]
    matrix.append(toprow)

    for i in strings:
        matrix.append([9] + [int(x) for x in i] + [9])

    botrow = [9 for _ in range(len(strings[0]) + 2)]
    matrix.append(botrow)

    return matrix

def grapher(matrix):
    graph = {}

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            adj = {}

            if i != 0 and j != 0 and i != len(matrix)-1 and j != len(matrix[0])-1:
                if i+1 != 0 and j != 0 and i+1 != len(matrix)-1 and j != len(matrix[0])-1:
                    adj.update({(i+1, j): matrix[i+1][j]})

                if i-1 != 0 and j != 0 and i-1 != len(matrix)-1 and j != len(matrix[0])-1:
                    adj.update({(i-1, j): matrix[i-1][j]})

                if i != 0 and j+1 != 0 and i != len(matrix)-1 and j+1 != len(matrix[0])-1:
                    adj.update({(i, j+1): matrix[i][j+1]})

                if i != 0 and j-1 != 0 and i != len(matrix)-1 and j-1 != len(matrix[0])-1:
                    adj.update({(i, j-1): matrix[i][j-1]})

            if adj != {}:
                graph.update({(i, j): adj})

    return graph

def dijkstra(graph, start, end):
    shortest = {}
    track = {}
    unseen = graph
    inf = 9999999999999999999999
    path = []

    for node in unseen:
        shortest[node] = inf
    shortest[start] = 0

    while unseen:
        min_dist = None
        count = -1

        for node in unseen:
            count += 1
            if min_dist is None:
                min_dist = node

            elif shortest[node] < shortest[min_dist]:
                min_dist = node
            
        options = graph[min_dist].items()
        
        for child, weight in options:
            if weight + shortest[min_dist] < shortest[child]:
                shortest[child] = weight + shortest[min_dist]
                track[child] = min_dist
        
        unseen.pop(min_dist)

    current = end

    while current != start:
        path.insert(0, current)
        current = track[current]

    path.insert(0, start)

    return shortest[end]

def sol1(inputs):
    matrix = grid(inputs)
    graph = grapher(matrix)
    val = dijkstra(graph, (1,1), (len(matrix) - 2, len(matrix) - 2))

    return val

def grid2(inputs):
    strings = process(inputs)
    matrix = []
    matrix2 = []

    for i in strings:
        matrix.append([int(x) for x in i])

    for i in matrix:
        row = i
        old = i

        for _ in range(4):
            new = []

            for x in old:
                if x == 9:
                    new.append(1)

                else:
                    new.append(x+1)

            old = new
            row += new

        matrix2.append(row)

    for i in range(4):
        for j in range(len(matrix)):
            new = [x + 1*(i+1) for x in matrix2[j]]

            for k in range(len(new)):
                if new[k] > 9:
                    new[k] -= 9
        
            matrix2.append(new)

    matrix3 = []
    toprow = [9 for _ in range(len(matrix2[0]) + 2)]
    matrix3.append(toprow)

    for i in matrix2:
        matrix3.append([9] + i + [9])

    botrow = [9 for _ in range(len(matrix2[0]) + 2)]
    matrix3.append(botrow)

    return matrix3

def sol2(inputs):
    matrix = grid2(inputs)
    graph = grapher(matrix)
    val =  dijkstra(graph, (1,1), (len(matrix) - 2, len(matrix) - 2))

    return val

def main():
    inputs = "15.txt"

    solution1 = sol1(inputs)
    solution2 = sol2(inputs) # this may have taken like an hour :skull:

    print(f"For Puzzle 1: {solution1}")
    print(f"For Puzzle 2: {solution2}")

if __name__ == "__main__":
    main()