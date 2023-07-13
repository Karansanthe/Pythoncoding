n = 16

if n == 0:
    print('No')
else:
    while n != 1:
        if n % 2 != 0:
            print('No')
            break
        n = n // 2
    else:
        print('Yes')

# using bit

n = 8

if(n & (n-1)) == 0:
    print("Yes")
else:
    print("No")

"""
In the given code snippet, the else statement after the while loop is not directly associated 
with the preceding if statement. Instead, it is associated with the while loop itself.

In Python, the else keyword can be used with a loop statement, such as while or for. 
The else block of code after a loop executes when the loop has completed all its iterations, 
but only if the loop was not terminated by a break statement."""