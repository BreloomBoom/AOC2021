from statistics import median

def process(file):
    f = open(file, "r")
    strings = f.read().split()
    f.close()

    return strings

def remove_obvious(string):
    resolved = ["<>", "{}", "[]", "()"]

    for i in resolved:
        while i in string:
            string = string.replace(i, "")
            string = remove_obvious(string)

    return string

def remove(string, illegals):
    string = remove_obvious(string)
    open_brackets = ["<", "{", "[", "("]
    closed_brackets = [">", "}", "]", ")"]

    for i in open_brackets:
        for j in closed_brackets:
            while i + j in string:
                illegals.append(j)
                string = string.replace(i + j, "")
                string = remove(string, illegals)

    return string

def illegal(input):
    strings = process(input)
    illegals = []

    for i in range(len(strings)):
        strings[i] = remove(strings[i], illegals)

    return illegals

def score1(input):
    illegals = illegal(input)
    total = 0

    for i in illegals:
        if i == ")":
            total += 3

        if i == "]":
            total += 57

        if i == "}":
            total += 1197

        if i == ">":
            total += 25137

    return total

def filterer(input):
    strings = process(input)
    closed_brackets = [">", "}", "]", ")"]
    vibe_checked = []

    for i in range(len(strings)):
        strings[i] = remove_obvious(strings[i])

        if all(x not in strings[i] for x in closed_brackets):
            vibe_checked.append(strings[i])

    return vibe_checked

def score2(input):
    strings = filterer(input)
    scores = []

    for i in strings:
        total = 0
        reverse = i[::-1]

        for j in reverse:
            if j == "(":
                total = total * 5 + 1

            if j == "[":
                total = total * 5 + 2

            if j == "{":
                total = total * 5 + 3

            if j == "<":
                total = total * 5 + 4

        scores.append(total)

    return median(scores)

def main():
    puzzle_input = "10.txt"

    solution1 = score1(puzzle_input)
    solution2 = score2(puzzle_input)

    print(f"For Puzzle 1: {solution1}")
    print(f"For Puzzle 1: {solution2}")

if __name__ == "__main__":
    main()