#### Date - 31/08/2026

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
<br>

***Count no. of Digits -*** <br>
Take Log<sub>10</sub> Num = x <br>
x + 1 = number of digits in Num
```
import math
num = 455
digits = int(math.log(num, 10) + 1)
print(f"No. of digits are {digits}")
```
*math.log(number, base)*

**Time complexity** - O(log<sub>10</sub>N)
<br>

**If the number of iterations is dependent on divisions the time complexity will be logarithmic**