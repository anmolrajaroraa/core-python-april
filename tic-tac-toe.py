import random

print("Tic Tac Toe".center(100))
userChoice = input("Which one do you want to use (X or O) : ")
userChoice = "X" if userChoice == "X" or userChoice == "x" else "O"
cpuChoice = "O" if userChoice == "X" else "X"

gameProgress = [1, 2, 3, 4, 5, 6, 7, 8, 9]
availablePositions = [1, 2, 3, 4, 5, 6, 7, 8, 9]
winningPositions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [
    0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
turnsPlayed = 0
userTurn = True  # 1 means user, 2 means cpu
isGameOver = False
message = "Game draw"

gameBoard = f'''
        {gameProgress[0]} | {gameProgress[1]} | {gameProgress[2]}
        ---------
        {gameProgress[3]} | {gameProgress[4]} | {gameProgress[5]}
        ---------
        {gameProgress[6]} | {gameProgress[7]} | {gameProgress[8]}
    '''
print(gameBoard)

while not isGameOver and len(availablePositions) > 0:

    if userTurn:
        userInput = int(input("Enter the position number : "))
        if userInput not in availablePositions:
            print("Invalid choice")
            continue
        availablePositions.remove(userInput)
        gameProgress[userInput - 1] = userChoice
        turnsPlayed += 1
    else:
        cpuInput = random.choice(availablePositions)
        availablePositions.remove(cpuInput)
        gameProgress[cpuInput - 1] = cpuChoice

    if (turnsPlayed >= 3):
        for position in winningPositions:
            # position -> [0,1,2]
            # position -> [3,4,5]
            if gameProgress[position[0]] == gameProgress[position[1]] and gameProgress[position[1]] == gameProgress[position[2]]:
                isGameOver = True
                message = "User Won" if userTurn else "CPU won"
                break

    userTurn = not userTurn

    gameBoard = f'''
        {gameProgress[0]} | {gameProgress[1]} | {gameProgress[2]}
        ---------
        {gameProgress[3]} | {gameProgress[4]} | {gameProgress[5]}
        ---------
        {gameProgress[6]} | {gameProgress[7]} | {gameProgress[8]}
    '''
    print(gameBoard)

print(message)

# if str.index('python') >= 0:
#     print('python found')
# if userInput in availablePositions: print("Valid choice")
# in, not in operators - membership operators
# for position in availablePositions:
#     if position == userInput:
#         print("Valid choice")
