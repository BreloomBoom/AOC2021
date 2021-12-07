depths = open("1.txt", "r")
depthslist = depths.read().split()
depths.close()

current = int(depthslist[0])
depthslist.remove(str(current))
increasing = 0

for i in depthslist:
    no = int(i)

    if current < no:
        increasing = increasing + 1

    current = no

print(increasing)