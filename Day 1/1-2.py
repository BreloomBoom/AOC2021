depths = open("1.txt", "r")
depthslist = depths.read().split()
depths.close()

depthslist = list(map(int, depthslist))
truedepth = []

for i in range(0,1998):
    truedepth.append(depthslist[i] + depthslist[i+1] + depthslist[i+2])

current = truedepth[0]
truedepth.remove(current)
increasing = 0

for i in truedepth:
    if i > current:
        increasing += 1
    
    current = i

print(increasing)