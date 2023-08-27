board = [' ' for x in range(10)]


def printBoard(board):
    print('   |   |   ')
    print(' ' + board[1] + ' | '+board[2] + ' | ' + board[3])
    # print('   |   |   ')
    print('------------')
    print(('   |   |   '))
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
   # print(('   |   |   '))
    print('------------')
    print(('   |   |   '))
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    # print(('   |   |   '))


def insertLetter(letter, pos):
    board[pos] = letter


def spaceIsFree(pos):
    return board[pos] == ' '


def isWinner(bo, le):  # bo-board , le-length
    return (bo[1] == le and bo[2] == le and bo[3] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or (bo[7] == le and bo[8] == le and bo[9] == le) or (bo[1] == le and bo[4] == le and bo[7] == le) or (bo[2] == le and bo[5] == le and bo[8] == le) or (bo[3] == le and bo[6] == le and bo[9] == le) or (bo[1] == le and bo[5] == le and bo[9] == le) or (bo[3] == le and bo[5] == le and bo[7] == le)


def playerMove():
    run = True
    while run:
        move = input("Please select a position to place an 'X' (1-9) : ")
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter('X', move)
                else:
                    print("Sorry, this place is occupied")
            else:
                print("PLease enter a number within range 0-9")
        except:
            print("Please type a number!")


def compMove():
    '''Herewe follow a 5 step algorithm
    -- first we will check if there's a move that the computer can do 
    so that it will win. 
    -- secondly we check if there's a move that will let the player win, 
    if there is then we block that place so as to not let the player win
    -- third, computer can't win and the player can't win so it's not as important
    where the computer move is
    -- so we check if the corners are all filled up, if no corners available,
    -- we check if the center's been taken, if not we take the center
    -- or we will move to any open edge'''
    possibleMoves = [x for x, letter in enumerate(
        board) if letter == ' ' and x != 0]  # enumerate gives us the indices as well as the values of the list
    move = 0

    for let in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i
                return move

    cornersOpen = []
    for i in possibleMoves:
        if i in [1, 3, 7, 9]:
            cornersOpen.append(i)
    if 5 in possibleMoves:
        move = 5
        return move
        
    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move
        
    edgesOpen = []
    for i in possibleMoves:
        if i in [2, 4, 6, 8]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)

    return move


def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]


def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True


def main():
    print("Welcome to Tic Tac Toe!")
    printBoard(board)

    while not (isBoardFull(board)):
        if not (isWinner(board, 'O')):
            playerMove()
            printBoard(board)
        else:
            print("'O' won this time!")
            break

        if not (isWinner(board, 'X')):
            move = compMove()
            if move == 0:
                print("Tie Game!")
            else:
                insertLetter('O', move)
                print("Computer places an 'O' in position ", move, ': ')
                printBoard(board)
        else:
            print("'X' won this time! Good Job!")
            break

    if isBoardFull(board):
        print("Tie Game!")


main()
while True:
    answer = input("Do you want to play again (Y/N)")
    if answer.lower() == 'y' or answer.lower == 'yes':
        board = [' ' for x in range(0, 10)]
        print("-------------------------------------")
        main()
    else:
        break
