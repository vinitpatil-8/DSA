n = int(input())

# 1 - Print name N times

print("Print name N times")
def printNTimes(name, count=0):
    if count>=n:
        return
    print(name)
    printNTimes(name, count + 1)
printNTimes('vinit')

# 2 - Print Linearly from 1 to N

print("Print Linearly from 1 to N")
def printTillN(count=1):
    if count>n:
        return
    print(count)
    printTillN(count+1)
printTillN()

# 3 - Print Linearly from N to 1

print("Print Linearly from N to 1")
def printTillN(count=n):
    if count<1:
        return
    print(count)
    printTillN(count-1)
printTillN()


# 4 - Backtracking 1 to N
print("Backtracking 1 to N")
def backtrack(i, n):
    if i<1:
        return
    backtrack(i-1, n)
    print(i)
backtrack(n, n)

# 5 - Backtracking N to 1
print("Backtracking N to 1")
def backtrackNto1(n, i=1):
    if i>n:
        return
    backtrackNto1(n, i+1)
    print(i)
backtrackNto1(n)

# 6 - Sum of first N numbers - parameterised
print("Sum of first N numbers - parameterised")
def sum(i, total=0):
    if i<1:
        print(total)
        return
    sum(i-1, total=total+i)
sum(n)

# 7 - Sum of first N numbers - functional
print("Sum of first N numbers - functional")
def sumf(i):
    if i==0:
        return 0
    return i + sumf(i-1)
print(sumf(n))

# 8 - Factorial of N (1x2x3x.......N) - parameterised
print("Factorial of N - parameterised")
def factorial(i, fact=1):
    if i<1:
        print(fact)
        return
    factorial(i-1, fact=fact*i)
factorial(n)

# 9 - Factorial of N (1x2x3x.......N) - functional
print("Factorial of N - functional")
def factorialf(i):
    if i==1:
        return i
    return i*factorialf(i-1)
print(factorialf(n))