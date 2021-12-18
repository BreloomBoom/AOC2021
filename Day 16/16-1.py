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

def main():
    inputs = "16.txt"

    solution1 = sol(inputs)

    print(f"For Puzzle 1: {solution1}")

if __name__ == "__main__":
    main()