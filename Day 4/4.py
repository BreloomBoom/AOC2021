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
    board = boards[minindex]

    return board

def maxboard(boards, numbers):
    turnlist = []

    for i in boards:
        a, b, c = endboard(i, numbers)
        turnlist.append(b)

    maxturns = max(turnlist)
    maxindex = turnlist.index(maxturns)
    board = boards[maxindex]

    return board

def score(board, numbers):
    finishedboard, b, lastnostr = endboard(board, numbers)
    lastno = int(lastnostr)
    total = sum(finishedboard)
    score = total * lastno

    return score

def main():
    f = open("4.txt", "r")
    boards = f.read().split("\n\n")
    numbers = boards.pop(0).split(",")
    f.close()
    
    score1 = score(minboard(boards, numbers), numbers)
    score2 = score(maxboard(boards, numbers), numbers)

    print(f"For Puzzle 1: {score1}")
    print(f"For Puzzle 2: {score2}")

if __name__ == "__main__":
    main()