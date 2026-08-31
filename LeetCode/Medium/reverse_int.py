x = int(input())
if not x <= 2**31 - 1 or not x >= -2**31:
    print(0) 
num = 0
negative = 0
if x<0:
    x = abs(x)
    negative += 1 
while x>0:
    digit = x%10
    x = int(x/10)
    num = num * 10 + (digit)
if not num <= 2**31 - 1 or not num >= -2**31:
    print(0)
elif negative == 0:
    print(num)
else:
    print(num - num*2)