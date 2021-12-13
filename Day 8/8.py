from copy import deepcopy
import re
 
def process(file):
    f = open(file, "r")
    strings = f.read()
    f.close()

    return strings

def filterer(strings):
    splitinput = re.split("\n|\|", deepcopy(strings)) 
    filtered = [x for x in splitinput if splitinput.index(x) % 2 != 0]
    filtered2 = [x for x in splitinput if splitinput.index(x) % 2 == 0]

    return filtered, filtered2
    
def p1_1478(filtered):
    times = 0

    for i in filtered:
        numbers = i.split()

        for j in numbers:
            if len(j) == 2 or len(j) == 3 or len(j) == 4 or len(j) == 7:
                times += 1

    return times

def decypher(digits):
    decyphered = ["x" for x in range(10)]
    numbers = digits.split()
    five_segments = [x for x in numbers if len(x) == 5]
    six_segments = [x for x in numbers if len(x) == 6]
    
    for i in numbers:
        if len(i) == 2:
            decyphered[1] = sorted(i)

        if len(i) == 3:
            decyphered[7] = sorted(i)

        if len(i) == 4:
            decyphered[4] = sorted(i)

        if len(i) == 7:
            decyphered[8] = sorted(i)

    adg = list(set(five_segments[0])&set(five_segments[1])&set(five_segments[2]))
    d = [x for x in adg if x in decyphered[4]][0]
    b = [x for x in decyphered[4] if x not in decyphered[1] and x != d][0]
    abfg = list(set(six_segments[0])&set(six_segments[1])&set(six_segments[2]))

    for i in five_segments:
        if decyphered[1][1] in i and decyphered[1][0] in i:
            decyphered[3] = sorted(i)

        elif b in i:
            decyphered[5] = sorted(i)

        else:
            decyphered[2] = sorted(i)

    for i in six_segments:
        remaining = [x for x in i if x not in abfg]

        if d in remaining:
            if decyphered[1][1] in remaining or decyphered[1][0] in remaining:
                decyphered[9] = sorted(i)

            else:
                decyphered[6] = sorted(i)

        else:
            decyphered[0] = sorted(i)

    return decyphered

def four_digit(decyphered, quad_no):
    digit_list = quad_no.split()
    digits = []

    for i in digit_list:
        for j in decyphered:
            if sorted(i) == j:
                digits.append(decyphered.index(j))
    
    a, b, c, d = digits

    number = a*1000 + b*100 + c*10 + d

    return number

def sumup(filtered, filtered2):
    total = 0

    for i in range(len(filtered)):
        decyphered = decypher(filtered2[i])
        number = four_digit(decyphered, filtered[i])
        total += number

    return total

def main():
    inputs = process("8.txt")
    filter1 = filterer(inputs)[0]
    filter2 = filterer(inputs)[1]
    times = p1_1478(filter1)
    total = sumup(filter1, filter2)

    print(f"For Puzzle 1: {times}")
    print(f"For Puzzle 2: {total}")

if __name__ == "__main__":
    main()
