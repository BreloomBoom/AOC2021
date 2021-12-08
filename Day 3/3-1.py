f = open("3.txt", "r")
binary = f.read().split()
f.close()

gamma = ""
epsilon = ""

for i in range(len(binary[0])):
    zero = 0
    one = 0

    for j in binary:
        if j[i] == "1":
            one += 1

        else:
            zero += 1

    if zero > one:
        gamma += "0"
        epsilon += "1"

    else:
        gamma += "1"
        epsilon += "0"

gammaint = int(gamma, 2)
epsilonint = int(epsilon, 2)
power = gammaint * epsilonint

print(power)