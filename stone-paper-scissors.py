import random

userWins = 0
cpuWins = 0
drawMatches = 0

while userWins < 3 and cpuWins < 3:
    print('''
        1. Stone
        2. Paper
        3. Scissors
    ''')
    userChoice = int(input("Enter your choice : "))
    if userChoice < 1 or userChoice > 3:
        continue
    cpuChoice = random.randint(1, 3)
    print(f"CPU choice : {cpuChoice}")
    if (userChoice == cpuChoice):
        drawMatches += 1
    elif userChoice == 1:
        if cpuChoice == 2:
            cpuWins += 1
        else:
            userWins += 1
    elif userChoice == 2:
        pass
    else:
        pass

    print(
        f"Score: User - {userWins}, CPU - {cpuWins}, Draw - {drawMatches}, Total Matches Played - {userWins + cpuWins + drawMatches}")


'''
stone stone - draw
stone paper - cpu wins
stone scissors
paper stone
paper paper - draw
paper scissors
scissors stone
scissors paper
scissors scissors - draw
'''
