def process(file):
    f = open(file, "r")
    strings = f.read().split()
    f.close()

    return strings

def grid(input):
    strings = process(input)
    matrix =[]
    toprow = ["x" for x in range(len(strings[0]) + 2)]
    matrix.append(toprow)

    for i in strings:
        listed = list(i)
        listed.append("x")
        listed.insert(0, "x")

        matrix.append(listed)

    botrow = ["x" for x in range(len(strings[0]) + 2)]
    matrix.append(botrow)

    return matrix

def flash_b(strings, flashes, i, j, tested):
    flashes = flash_a(strings, flashes, i+1, j, tested)
    flashes = flash_a(strings, flashes, i-1, j, tested)
    flashes = flash_a(strings, flashes, i+1, j+1, tested)
    flashes = flash_a(strings, flashes, i+1, j-1, tested)
    flashes = flash_a(strings, flashes, i-1, j+1, tested)
    flashes = flash_a(strings, flashes, i-1, j-1, tested)
    flashes = flash_a(strings, flashes, i, j+1, tested)
    flashes = flash_a(strings, flashes, i, j-1, tested)

    return flashes

def flash_a(strings, flashes, i, j, tested):
    if strings[i][j] != "x":
        if strings[i][j] == "9":
            strings[i][j] = "f"
            flashes += 1
            tested.append([i, j])
            flashes = flash_b(strings, flashes, i, j, tested)

        elif strings[i][j] == "f" and [i, j] not in tested:
            tested.append([i, j])
            flashes = flash_b(strings, flashes, i, j, tested)

        elif strings[i][j] == "f":
            pass

        else:
            strings[i][j] = str(int(strings[i][j])+1)
    
    return flashes

def flashgens(input, gens):
    strings = grid(input)
    flashes = 0

    for _ in range(gens):
        tested = []

        for i in range(len(strings)):
            for j in range(len(strings[i])):
                flashes = flash_a(strings, flashes, i, j, tested)

        for i in range(len(strings)):
            for j in range(len(strings[i])):
                if strings[i][j] == "f":
                    strings[i][j] = "0"

    return flashes

def check_all(string):
    if all(string[i] == "0" or string[i] == "x" for i in range(len(string))):
        return True

    return False

def all_flash(input):
    strings = grid(input)
    flashes = 0
    gens = 0

    while True:
        tested = []
        gens += 1

        for i in range(len(strings)):
            for j in range(len(strings[i])):
                flash_a(strings, flashes, i, j, tested)

        for i in range(len(strings)):
            for j in range(len(strings[i])):
                if strings[i][j] == "f":
                    strings[i][j] = "0"
                    
        if all(check_all(strings[i]) for i in range(len(strings))):
            return gens

def main():
    puzzle_input = "11.txt"

    solution1 = flashgens(puzzle_input, 100)
    solution2 = all_flash(puzzle_input)

    print(f"For Puzzle 1: {solution1}")
    print(f"For Puzzle 1: {solution2}")

if __name__ == "__main__":
    main()