# Find Greatest Common Divisor of Array
nums = [2,5,6,9,10] # dummy input
a = max(nums)
b = min(nums)
while a>0 and b>0:
    if a>b:
        a = a%b
    else:
        b = b%a
print(max(a, b))