# Import Necessary Libraries
import sys

def doSomething(n, m):
    # If there is only one tower, Player 1 wins
    if n == 1:
        return 1
    # If the height of each tower is 1, Player 1 wins
    elif m == 1:
        return 1
    # If the height of any tower is even, Player 2 wins
    elif m % 2 == 0:
        return 2
    # Otherwise, Player 1 wins
    else:
        return 1


# Take Input
inputVal1, inputVal2 = map(int, input().split())

# Process Output Using Function
outputVal = doSomething(inputVal1, inputVal2)

# Print Output
print(outputVal)
