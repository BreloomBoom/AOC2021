def process(file):
    f = open(file, "r")
    strings = f.read().split(",")
    numbers = [int(x) for x in strings]
    f.close()

    return numbers

def best(numbers, puzzle):
    fuel_list = []

    for i in range(0,max(numbers)+1):
        total = 0

        for j in numbers:
            if puzzle == 1:
                total += abs(j - i)

            if puzzle == 2:
                total += abs(j - i) * (abs(j - i) + 1) / 2

        fuel_list.append(total)

    best_fuel = int(min(fuel_list))

    return best_fuel

def main():
    positions = process("7.txt")
    fuel1 = best(positions, 1)
    fuel2 = best(positions, 2)

    print(f"For Puzzle 1: {fuel1}")
    print(f"For Puzzle 2: {fuel2}")

if __name__ == "__main__":
    main()