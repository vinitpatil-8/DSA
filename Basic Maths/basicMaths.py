import math
# Extracting all the digits (reverse fashion) -

n = 7789
extracted_digits = []
while n>0:
    lastDigit = n%10
    extracted_digits.append(lastDigit)
    n = int(n/10)
print(f"The digits are {extracted_digits}")


# Count no. of Digits - 
num = 455
digits = int(math.log(num, 10) + 1)
print(f"There are {digits} digits in {num}")

# Armstrong Number
armNum = 371
test = armNum
score = 0
while test>0:
    lastD = test%10
    score = score + (lastD*lastD*lastD)
    test = int(test/10)
if score == armNum:
    print(f"{armNum} is an Armstrong Number")
else:
    print(f"{armNum} isn't an Armstrong Number")

# Divisors
getDivisorNum = 100
divisors = []
for i in range (1, math.isqrt(getDivisorNum)+1):
    if getDivisorNum%i == 0:
        divisors.append(i)
        if i!=getDivisorNum//i:
            divisors.append(getDivisorNum//i)
divisors.sort()
print(f"The divisors of {getDivisorNum} are {divisors}")

# Prime Number
checkNum = 9973
verify = 0
for i in range(1, math.isqrt(checkNum)+1):
    if checkNum%i==0 and i!=1 and i!=checkNum:
        verify += 1 
        print(f"{checkNum} is not Prime")
        break 
if verify == 0:
    print(f"{checkNum} is Prime")

# GCD
num1 = 20 
num2 = 40
# for i in range(min(num1, num2), 0, -1): - one way of going reverse
for i in reversed(range((min(num1, num2)+1))):
    if num1%i==0 and num2%i==0:
        print(f"The GCD of {num1} and {num2} is {i}")
        break