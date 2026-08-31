num = int(input())
n = num
count = 0
while n>0:
    digit = n%10
    if num%digit == 0:
        count += 1
    n = int(n/10)
print(count)