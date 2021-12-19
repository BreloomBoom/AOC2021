def process(inputs):
    hex_to_bi = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111"
    }
    
    f = open(inputs, "r").read()
    binary = ""
    for i in f:
        binary += hex_to_bi[i]

    return binary

def packeter(string, versions):
    version = int(string[:3], 2)
    type_id = int(string[3:6], 2)
    string = string[6:]
    versions += version

    if type_id == 4:
        lit = ""
        while string[0] == "1":
            lit += string[1:5]
            string = string[5:]
        lit += string[1:5]
        string = string[5:]
        value = int(lit, 2)

        return string, versions, value

    else:
        values = []
        if string[0] == "0":
            string = string[1:]
            bit_len = int(string[:15], 2)
            string = string[15:]
            goal = string[bit_len:]
            while string != goal:
                string, versions, value = packeter(string, versions)
                values.append(value)

        elif string[0] == "1":
            string = string[1:]
            pack_len = int(string[:11], 2)
            string = string[11:]
            for _ in range(pack_len):
                string, versions, value = packeter(string, versions)
                values.append(value)

        if type_id == 0:
            final = sum(values)

        if type_id == 1:
            final = 1
            for i in values:
                final *= i

        if type_id == 2:
            final = min(values)

        if type_id == 3:
            final = max(values)

        if type_id == 5:
            if values[0] > values[1]:
                final = 1
            else:
                final = 0

        if type_id == 6:
            if values[0] < values[1]:
                final = 1
            else:
                final = 0

        if type_id == 7:
            if values[0] == values[1]:
                final = 1
            else:
                final = 0

        return string, versions, final

def sol(inputs):
    binary = process(inputs)
    versions = 0
    binary, versions, value = packeter(binary, versions)

    return versions, value

def main():
    inputs = "16.txt"

    solution1 = sol(inputs)[0]
    solution2 = sol(inputs)[1]

    print(f"For Puzzle 1: {solution1}")
    print(f"For Puzzle 2: {solution2}")

if __name__ == "__main__":
    main()