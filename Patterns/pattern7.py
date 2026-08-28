n = int(input())
for i in range(n):
    for j in range(2*n+1):
        if j<n-1:
            print("h", end='')
        elif j>n-1:
            print("h", end='')
        else:
            print("*", end='')    
    print()    
        # space - n-i
        # stars - 2*i+1
        # space - n-i