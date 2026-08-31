# Extracting all the digits (reverse fashion) -

n = 7789
while n>0:
    lastDigit = n%10
    print(lastDigit)
    n = int(n/10)