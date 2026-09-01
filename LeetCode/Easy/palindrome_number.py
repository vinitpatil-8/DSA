x = int(input())
num = 0
original_num = x
while original_num>0:
    digit = original_num%10
    original_num = int(original_num/10)
    num = num * 10 + digit
if num == x:
    print(True)
else:
    print(False)