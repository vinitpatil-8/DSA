n = int(input())
for i in range(1, 2*n):
    for j in range(1, 2*n+1):
        if i<=n:
            # stars
            if j<=i:
                print('*', end='')
        
            # space
            elif j<(2*n+1)-i:
                print(' ', end='')
            # stars
            else:
                print('*', end='')
        else:
            # stars
            if j<(2*n+1)-i:
                print('*', end='')
                    
            # space
            elif j<=i:
                print(' ', end='')
            # stars
            else:
                print('*', end='')
    print()