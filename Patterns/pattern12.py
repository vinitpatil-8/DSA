n = int(input())
for i in range(1, n+1):
    for j in range(1, n*2+1):
        if j<=i:
            print(j, end='')
        elif j>i and j<=(2*n-i):
            print(" ", end='')
        else:
            print((n*2+1)-j, end='')
    print()