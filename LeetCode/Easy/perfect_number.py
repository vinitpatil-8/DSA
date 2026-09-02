import math
num = int(input("Enter a number"))
i = 1
sumCheck = 0
while i <= math.isqrt(num):
    if num % i == 0:
        x = num / i
        if x == 1:
            sumCheck = sumCheck + i + x
        elif x != num:
            sumCheck = sumCheck + i + x
        else:
            sumCheck = sumCheck + i
    i = i + 1
if sumCheck == num:
    print(True)
else:
    print(False)