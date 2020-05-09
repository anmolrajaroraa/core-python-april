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
currentPlayer = 1  # 1 means user, 2 means cpu
isGameOver = False
while not isGameOver:
    gameBoard = f'''
        {gameProgress[0]} | {gameProgress[1]} | {gameProgress[2]}
        ---------
        {gameProgress[3]} | {gameProgress[4]} | {gameProgress[5]}
        ---------
        {gameProgress[6]} | {gameProgress[7]} | {gameProgress[8]}
    '''
    print(gameBoard)

    userInput = int(input("Enter the position number : "))
    if userInput not in availablePositions:
        print("Invalid choice")
        continue
    availablePositions.remove(userInput)
    gameProgress[userInput - 1] = userChoice
    turnsPlayed += 1
    if (turnsPlayed >= 3):
        for position in winningPositions:
            # position -> [0,1,2]
            # position -> [3,4,5]
            if gameProgress[position[0]] == gameProgress[position[1]] and gameProgress[position[1]] == gameProgress[position[2]]:
                isGameOver = True
    currentPlayer = 2

    # cpuInput = random.choice(availablePositions)
    # availablePositions.remove(cpuInput)
    # gameProgress[cpuInput - 1] = cpuChoice

    # if str.index('python') >= 0:
    #     print('python found')
    # if userInput in availablePositions: print("Valid choice")
    # in, not in operators - membership operators
    # for position in availablePositions:
    #     if position == userInput:
    #         print("Valid choice")
