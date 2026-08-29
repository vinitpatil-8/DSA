n = int(input())
for i in range(1, 2*n):
    stars = i
    if i>n:
        stars = 2*n - i

    for j in range(1, n+1):
        if j<=stars:
            print('*', end='')

    print()
