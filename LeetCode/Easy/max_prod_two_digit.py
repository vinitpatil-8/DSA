n = 134
digits = []
while n>0:
    lastDigit = n%10
    digits.append(lastDigit)
    n = int(n/10)
firstmax = max(digits)
digits.remove(firstmax)
print(firstmax * max(digits))