from copy import deepcopy

def process_file(textfile):
    f = open(textfile, "r")
    strings = f.read().split(",")
    numbers = [int(x) for x in strings]
    f.close()

    return numbers

def growth(fish, days):
    school = deepcopy(fish)

    while days != 0:
        for i in range(len(school)):
            if school[i] == 0:
                school.append(8)
                school[i] = 6

            else:
                school[i] -= 1

        days -= 1

    return school

def main():
    fish = process_file("6.txt")
    end1 = growth(fish, 80)
    population1 = len(end1)
    # end2 = growth(fish, 256)
    # population2 = len(end2)

    print(f"For Puzzle 1: {population1}")
    # print(f"For Puzzle 2: {population2}") population 2 requires 11tb in ram to do

if __name__ == "__main__":
    main()