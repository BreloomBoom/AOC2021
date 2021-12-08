f = open("3.txt", "r")
binary = f.read().split()
binary1 = binary
f.close()

for i in range(len(binary[0])):
    zero = 0
    one = 0
    
    for j in binary:
        if j[i] == "1":
            one += 1

        else:
            zero += 1

    if zero > one:
        binary = [x for x in binary if "0" in x[i]]

    else:
        binary = [x for x in binary if "1" in x[i]]

for i in range(len(binary1[0])):
    zero = 0
    one = 0
    
    for j in binary1:
        if j[i] == "1":
            one += 1

        else:
            zero += 1

    if zero > one:
        if len(binary1) != 1:
            binary1 = [x for x in binary1 if "1" in x[i]]

    else:
        if len(binary1) != 1:
            binary1 = [x for x in binary1 if "0" in x[i]]

o2 = binary[0]
co2 = binary1[0]
o2int = int(o2, 2)
co2int = int(co2, 2)
life = o2int * co2int

print(life)