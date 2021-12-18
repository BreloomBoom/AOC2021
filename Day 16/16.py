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
        while string[0] == "1":
            string = string[5:]
        string = string[5:]

        return string, versions

    else:
        if string[0] == "0":
            string = string[1:]
            bit_len = int(string[:15], 2)
            string = string[15:]
            while string != string[bit_len:] and not all(string[x] == "0" for x in range(len(string))) and string != "":
                string, versions = packeter(string, versions)

            return string, versions

        if string[0] == "1":
            string = string[1:]
            pack_len = int(string[:11], 2)
            string = string[11:]
            for _ in range(pack_len):
                while not all(string[x] == "0" for x in range(len(string))) and string != "":
                    string, versions = packeter(string, versions)

            return string, versions

def sol(inputs):
    binary = process(inputs)
    versions = 0
    while not all(binary[x] == "0" for x in range(len(binary))) and binary != "":
        binary, versions = packeter(binary, versions)

    return versions

def packeter2(string, versions):
    version = int(string[:3], 2)
    type_id = int(string[3:6], 2)
    string = string[6:]
    versions += version

    if type_id == 4:
        literal = ""
        while string[0] == "1":
            literal += string[1:5]
            string = string[5:]
        literal += string[1:5]
        string = string[5:]
        value = int(literal, 2)

        return string, versions, value

    if type_id == 0:
        values = 0

        if string[0] == "0":
            string = string[1:]
            bit_len = int(string[:15], 2)
            string = string[15:]
            while string != string[bit_len:] and not all(string[x] == "0" for x in range(len(string))) and string != "":
                string, versions, value = packeter2(string, versions)
                values += value

        if string[0] == "1":
            string = string[1:]
            pack_len = int(string[:11], 2)
            string = string[11:]
            for _ in range(pack_len):
                if not all(string[x] == "0" for x in range(len(string))) and string != "":
                    string, versions, value = packeter2(string, versions)
                    values += value

        return string, versions, values

    if type_id == 1:
        values = 1

        if string[0] == "0":
            string = string[1:]
            bit_len = int(string[:15], 2)
            string = string[15:]
            while string != string[bit_len:] and not all(string[x] == "0" for x in range(len(string))) and string != "":
                string, versions, value = packeter2(string, versions)
                values *= value

        if string[0] == "1":
            string = string[1:]
            pack_len = int(string[:11], 2)
            string = string[11:]
            for _ in range(pack_len):
                if not all(string[x] == "0" for x in range(len(string))) and string != "":
                    string, versions, value = packeter2(string, versions)
                    values *= value

        return string, versions, value

    if type_id == 2:
        values = []

        if string[0] == "0":
            string = string[1:]
            bit_len = int(string[:15], 2)
            string = string[15:]
            while string != string[bit_len:] and not all(string[x] == "0" for x in range(len(string))) and string != "":
                string, versions, value = packeter2(string, versions)
                values.append(value)

        if string[0] == "1":
            string = string[1:]
            pack_len = int(string[:11], 2)
            string = string[11:]
            for _ in range(pack_len):
                if not all(string[x] == "0" for x in range(len(string))) and string != "":
                    string, versions, value = packeter2(string, versions)
                    values.append(value)

        return string, versions, min(values)

    if type_id == 3:
        values = []

        if string[0] == "0":
            string = string[1:]
            bit_len = int(string[:15], 2)
            string = string[15:]
            while string != string[bit_len:] and not all(string[x] == "0" for x in range(len(string))) and string != "":
                string, versions, value = packeter2(string, versions)
                values.append(value)

        if string[0] == "1":
            string = string[1:]
            pack_len = int(string[:11], 2)
            string = string[11:]
            for _ in range(pack_len):
                if not all(string[x] == "0" for x in range(len(string))) and string != "":
                    string, versions, value = packeter2(string, versions)
                    values.append(value)

        return string, versions, max(values)

    if type_id == 5:
        values = []

        if string[0] == "0":
            string = string[1:]
            string = string[11:]
            for _ in range(2):
                if not all(string[x] == "0" for x in range(len(string))) and string != "":
                    string, versions, value = packeter2(string, versions)
                    values.append(value)

        if string[0] == "1":
            string = string[1:]
            string = string[11:]
            for _ in range(2):
                if not all(string[x] == "0" for x in range(len(string))) and string != "":
                    string, versions, value = packeter2(string, versions)
                    values.append(value)

        if values[0] > values[1]:
            return string, versions, 1

        else:
            return string, versions, 0

    if type_id == 6:
        values = []

        if string[0] == "0":
            string = string[1:]
            string = string[11:]
            for _ in range(2):
                if not all(string[x] == "0" for x in range(len(string))) and string != "":
                    string, versions, value = packeter2(string, versions)
                    values.append(value)

        if string[0] == "1":
            string = string[1:]
            string = string[11:]
            for _ in range(2):
                if not all(string[x] == "0" for x in range(len(string))) and string != "":
                    string, versions, value = packeter2(string, versions)
                    values.append(value)

        if values[0] < values[1]:
            return string, versions, 1

        else:
            return string, versions, 0

    if type_id == 7:
        values = []

        if string[0] == "0":
            string = string[1:]
            string = string[11:]
            for _ in range(2):
                if not all(string[x] == "0" for x in range(len(string))) and string != "":
                    string, versions, value = packeter2(string, versions)
                    values.append(value)

        if string[0] == "1":
            string = string[1:]
            string = string[11:]
            for _ in range(2):
                if not all(string[x] == "0" for x in range(len(string))) and string != "":
                    string, versions, value = packeter2(string, versions)
                    values.append(value)

        if values[0] == values[1]:
            return string, versions, 1

        else:
            return string, versions, 0

def sol2(inputs):
    binary = process(inputs)
    versions = 0
    while not all(binary[x] == "0" for x in range(len(binary))) and binary != "":
        binary, versions, value = packeter2(binary, versions)

    return versions, value

def main():
    inputs = "16.txt"

    solution1 = sol(inputs)
    # solution2 = sol2(inputs)

    print(f"For Puzzle 1: {solution1}")
    # print(f"For Puzzle 2: {solution2}")

if __name__ == "__main__":
    main()