instructions = open("2.txt", "r")
directions = instructions.read().split("\n")
instructions.close()

x = 0
y = 0

for i in directions:
    j = i.split()
    if j[0] == "forward":
        x += int(j[1])
    
    if j[0] == "up":
        y -= int(j[1])

    if j[0] == "down":
        y += int(j[1])

print(x*y)