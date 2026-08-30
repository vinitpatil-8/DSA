n = int(input())
for i in range(1, 2*n):
    for j in range(1, 2*n):
        top = i-1
        left = j-1
        right = (2*n-1) - j
        bottom = (2*n-1) - i
        print(n-min(top, left, right, bottom), end=' ')
    print()