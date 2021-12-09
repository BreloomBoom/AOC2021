def process_file(textfile):
    f = open(textfile, "r")
    strings = f.read().split(",")
    numbers = [int(x) for x in strings]
    f.close()

    return numbers

def list_to_data(numbers):
    data = [numbers.count(i) for i in range(0,9)]

    return data

def population(data, days):
    for i in range(days):
        new = data[0]
        data[0] = data[1]
        data[1] = data[2]
        data[2] = data[3]
        data[3] = data[4]
        data[4] = data[5]
        data[5] = data[6]
        data[6] = data[7] + new
        data[7] = data[8]
        data[8] = new
    
    return sum(data)

def main():
    fish = process_file("6.txt")
    initial = list_to_data(fish)
    final = population(initial, 256)

    print(f"For Puzzle 2: {final}") 

if __name__ == "__main__":
    main()