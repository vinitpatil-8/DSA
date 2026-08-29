n = int(input())
for i in range(n):
    for a in range(i):
        print(" ", end='')
    for b in range(2*(n-i)-1):
        print("*", end='')
    for c in range(i):
        print(" ", end='')
          
    print()   