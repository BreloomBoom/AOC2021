def process(inputs):
    f = open(inputs, "r")
    template, rulesblock = f.read().split("\n\n")
    f.close()

    rules = []
    for i in rulesblock.split("\n"):
        rules.append(i.split(" -> "))

    return template, rules

def insertion(template, rules, new, i):
    pair = template[i] + template[i+1]

    for j in rules:
        if j[0] == pair:
            new += template[i] + j[1]
            return new

    new += template[i]
    return new

def generations(inputs, gens):
    template, rules = process(inputs)

    for _ in range(gens):
        new = ""

        for i in range(len(template)):
            if i < len(template) - 1:
                new = insertion(template, rules, new, i)

            else:
                new += template[i]

        template = new

    return template

def diff(inputs, gens):
    template = generations(inputs, gens)
    count = {}

    for i in template:
        if i not in count:
            count.update({i: 1})

        else:
            count[i] += 1

    max_no = 0
    min_no = count[template[0]]

    for i in count:
        if max_no < count[i]:
            max_no = count[i]

        if min_no > count[i]:
            min_no = count[i]

    return max_no - min_no

def main():
    inputs = "test.txt"

    solution1 = diff(inputs, 10)
    # solution2 = diff(inputs, 40)

    print(f"For Puzzle 1: {solution1}")
    # print(f"For Puzzle 2: {solution2}") i did not learn from the lanternfish

if __name__ == "__main__":
    main()