# pattern 1
'''
*
**
***
****
*****
'''
for i in range(5):
    for j in range(i + 1):
        print("*", end='')
    print()

'''
*****
****
***
**
*
'''

for i in range(5):
    for j in range(5 - i):
        print("*", end='')
    print()

# i *
# 0 -> 5
# 1 -> 4
# 2 -> 3
# 3 -> 2
# 4 -> 1

# 5 - i -> 1

'''
    *         -> 4 spaces 1 star
   ***      -> 3 spaces 3 star
  *****       -> 2 spaces 5 star
 *******
*********
'''
# 0 -> 1
# 1 -> 3
# 2 * 2 + 1 -> 5

# (2 * i) + 1 = 3

'''
    *         
   **      
  ***     
 ****
*****
'''
for i in range(5):
    for j in range(4 - i):
        print(" ", end="")
    for k in range((2 * i) + 1):
        print("*", end="")
    print()

'''
*********
 *******
  *****
   ***
    *
'''
print("\n____________________\n")

for i in range(5):
    for j in range(i):
        print(" ", end="")
    for k in range(9 - (2 * i)):
        print("*", end="")
    print()


'''
    *         
   ***      
  *****       
 *******
*********
 *******
  *****
   ***
    *
'''
for i in range(9):
    if i <= 4:
        for j in range(4 - i):
            print(" ", end="")
        for k in range((2 * i) + 1):
            print("*", end='')
    else:
        for j in range(i - 4):
            print(" ", end="")
        for k in range(((9 - i) * 2) - 1):
            print("*", end="")
    print()

# Version 2 for diamond
print("\n____________________\n")
for i in range(5):
    for j in range(4 - i):
        print(" ", end="")
    for k in range((2 * i) + 1):
        print("*", end="")
    print()
for i in range(5):
    if i == 0:
        continue
    for j in range(i):
        print(" ", end="")
    for k in range(9 - (2 * i)):
        print("*", end="")
    print()


'''
0 - 1
1 - 3
2 - 5
3 - 7
4 - 9
5 - 7 
6 - 5 
7 - 3 
8 - 1 

((9 - i) * 2) - 1

5 -> 7
6 -> 5
7 -> 3
8 -> 1

7 - 2 * i
'''
