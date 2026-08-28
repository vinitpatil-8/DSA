n = int(input())
for i in range(n):
    for a in range(n-i):
        print(" ", end='')
    for b in range(2*i+1):
        print("*", end='')
    for c in range(n-i):
        print(" ", end='')
          
    print()    
        # space - n-i
        # stars - 2*i+1
        # space - n-i