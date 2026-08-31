import math
# Extracting all the digits (reverse fashion) -

n = 7789
while n>0:
    lastDigit = n%10
    print(lastDigit)
    n = int(n/10)

# Count no. of Digits - 
num = 455
digits = int(math.log(num, 10) + 1)
print(f"No. of digits are {digits}")
