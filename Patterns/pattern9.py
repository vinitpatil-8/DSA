n = int(input())
for i in range(n):
    for a in range(n-i-1):
        print(" ", end='')
    for b in range(2*i+1):
        print("*", end='')
    for c in range(n-i-1):
        print(" ", end='')
    print()


for i in range(n):
    for p in range(i):
            print(" ", end='')
    for q in range(2*(n-i)-1):
            print("*", end='')
    for r in range(i):
            print(" ", end='')
          
    print()  