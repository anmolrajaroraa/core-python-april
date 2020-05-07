'''
*
**
***
****
*****
'''

# String replication
print("hello" * 10)

for i in range(5):
    print("*" * (i + 1))

'''
    *         
   ***      
  *****       
 *******
*********
'''

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
        print(" " * (4 - i), end="")
        print("*" * ((2 * i) + 1))
    else:
        print(" " * (i - 4), end="")
        print("*" * (((9 - i) * 2) - 1))
