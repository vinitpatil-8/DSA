# 1 - Print name N times
n = int(input())
def printNTimes(name, count=0):
    if count>=n:
        return
    print(name)
    printNTimes(name, count + 1)
printNTimes('vinit')

# 2 -