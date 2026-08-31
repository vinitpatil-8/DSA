#### Date - 28/08/2026

# Basic Math Concepts

## Extracting Digits - 

To get Digits of a number start by using '%' operator by 10 and then divide by 10 and keep using '%10' until you get all digits <br>
***Code Example -***
```
n = 7789
while n>0:
    lastDigit = n%10
    print(lastDigit)
    n = int(n/10)
```