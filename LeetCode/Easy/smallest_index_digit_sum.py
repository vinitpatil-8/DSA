nums = [619,916,21,4,4,835]
eligibleNums = []
for b, a in enumerate(nums):
    sum = 0
    while a>0:
        lastDigit = a%10
        sum = sum + lastDigit
        a = int(a/10)
    if sum == b:
        eligibleNums.append(b)
if not eligibleNums:
    print(-1)
else:
    smallest = min(eligibleNums)
    print(smallest)