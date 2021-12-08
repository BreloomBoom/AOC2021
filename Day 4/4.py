def tomatrix(rawboard):
    board = []

    for i in rawboard.split("\n"):
        board.append(i.split())

    return board

def win(board):
    for i in range(len(board)):
        if board[i] == [x for x in board[i] if x == board[i][0]]:
            return True

        if all(board[0][i] == board[j][i] for j in range(5)):
            return True

    return False

def endboard(rawboard, numbers):
    turns = 0
    lastno = ""
    board = tomatrix(rawboard)

    for i in numbers:
        if win(board) == False:
            turns += 1

            for j in range(len(board)):
                for k in range(len(board[j])):
                    if board[j][k] == i:
                        board[j][k] = "x"
                        lastno = i

    return board, turns, lastno

def sum(board):
    total = 0

    for i in board:
        for j in i:
            if j != "x":
                total += int(j)

    return total

def minboard(boards, numbers):
    turnlist = []

    for i in boards:
        a, b, c = endboard(i, numbers)
        turnlist.append(b)

    minturns = min(turnlist)
    minindex = turnlist.index(minturns)

    return minindex  

def maxboard(boards, numbers):
    turnlist = []

    for i in boards:
        a, b, c = endboard(i, numbers)
        turnlist.append(b)

    maxturns = max(turnlist)
    maxindex = turnlist.index(maxturns)

    return maxindex  

def main():
    f = open("4.txt", "r")
    boards = f.read().split("\n\n")
    f.close()
    numbers = boards.pop(0).split(",")

    boardindex1 = minboard(boards, numbers)
    board1 = boards[boardindex1]
    finishedboard1, b1, lastnostr1 = endboard(board1, numbers)
    lastno1 = int(lastnostr1)
    total1 = sum(finishedboard1)
    score1 = lastno1 * total1

    print(f"For Puzzle 1: {score1}")

    boardindex2 = maxboard(boards, numbers)
    board2 = boards[boardindex2]
    finishedboard2, b2, lastnostr2 = endboard(board2, numbers)
    lastno2 = int(lastnostr2)
    total2 = sum(finishedboard2)
    score2 = lastno2 * total2

    print(f"For Puzzle 2: {score2}")

if __name__ == "__main__":
    main()