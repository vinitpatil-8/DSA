n = int(input())
for i in range(1, n+1):
    for j in range(1, n+1):
        if j<=i:
            if i%2!=0 and j%2!=0:
                print('1', end=' ')
            elif i%2!=0 and j%2==0:
                print('0', end=' ')
            elif i%2==0 and j%2!=0:
                print('0', end=' ')
            elif i%2==0 and j%2==0:
                print('1', end=' ')

    print()   