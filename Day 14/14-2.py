from copy import deepcopy

def process(inputs):
    f = open(inputs, "r")
    template, rulesblock = f.read().split("\n\n")
    f.close()

    rules = []
    for i in rulesblock.split("\n"):
        rules.append(i.split(" -> "))

    count = {}
    for i in rules:
        count.update({i[0]: 0})

    for i in range(len(template)):
        if i < len(template) - 1:
            count[template[i] + template[i+1]] += 1

    return rules, count, template[0], template[len(template)-1]

def generations(inputs, gens):
    rules, count, start, end = process(inputs)

    for _ in range(gens):
        count2 = deepcopy(count)

        for i in count2:
            count2[i] = 0

        for i in rules:
            count2[i[0][0]+i[1]] += count[i[0]]
            count2[i[1]+i[0][1]] += count[i[0]]
        
        count = count2

    return count, start, end

def diff(inputs, gens):
    count, start, end = generations(inputs, gens)
    elements = {}

    for i in count:
        if i[0] not in elements:
            elements.update({i[0]: count[i]})

        else:
            elements[i[0]] += count[i]

        if i[1] not in elements:
            elements.update({i[1]: count[i]})

        else:
            elements[i[1]] += count[i]
    
    elements[start] += 1
    elements[end] += 1
    
    max_no = 0
    min_no = elements[start]

    for i in elements:
        if max_no < elements[i]:
            max_no = elements[i]

        if min_no > elements[i]:
            min_no = elements[i]

    return int((max_no - min_no)/2)

def main():
    inputs = "14.txt"

    solution1 = diff(inputs, 10)
    solution2 = diff(inputs, 40)

    print(f"For Puzzle 1: {solution1}")
    print(f"For Puzzle 2: {solution2}")

if __name__ == "__main__":
    main()