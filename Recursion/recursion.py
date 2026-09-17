n = int(input())

# 1 - Print name N times

def printNTimes(name, count=0):
    if count>=n:
        return
    print(name)
    printNTimes(name, count + 1)
printNTimes('vinit')

# 2 - Print Linearly from 1 to N

def printTillN(count=1):
    if count>n:
        return
    print(count)
    printTillN(count+1)
printTillN()

# 3 - Print Linearly from N to 1

def printTillN(count=n):
    if count<1:
        return
    print(count)
    printTillN(count-1)
printTillN()
print("done")
# 4 - Backtracking

def backtrack(count=n):
    if count<1:
        return
    backtrack(count-1)
    print(count)
backtrack()