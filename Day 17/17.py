from math import ceil, sqrt

def process(inputs):
    f = open(inputs, "r").read()[15:]
    a, b = f.split(", y=")
    x = [int(i) for i in a.split("..")]
    y = [int(j) for j in b.split("..")]

    return x, y

def min_max_ux(x):
    max_ux = x[1]
    min_ux = ceil((-1+sqrt(1+8*x[0]))/2)

    return min_ux, max_ux

def step(x, y, vx, vy):
    if vx > 0:
        x += vx
    y += vy
    vx -= 1
    vy -= 1

    return x, y, vx, vy

def sol(inputs):
    hs = []
    a, b = process(inputs)
    min_ux, max_ux = min_max_ux(a)
    values = 0

    for i in range(b[0], -b[0]):
        for j in range(min_ux, max_ux + 1):
            vx, vy = j, i
            x, y = 0, 0
            max_y = 0
            passes = False
            while y >= b[0]:
                x, y, vx, vy = step(x, y, vx, vy)
                if y > max_y:
                    max_y = y

                if x in range(a[0], a[1]+1) and y in range(b[0], b[1]+1):
                    passes = True

            if passes:
                hs.append(max_y)
                values += 1

    return max(hs), values

def main():
    inputs = "17.txt"

    solution1 = sol(inputs)[0]
    solution2 = sol(inputs)[1]

    print(f"For Puzzle 1: {solution1}")
    print(f"For Puzzle 2: {solution2}")

if __name__ == "__main__":
    main()