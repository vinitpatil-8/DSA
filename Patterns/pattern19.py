n = int(input())
for i in range(n):
    for a in range(n-i):
        print("*", end='')
    for b in range(2*i):
        print(" ", end='')
    for c in range(n-i):
        print("*", end='')
    print()


for i in range(n):
    for p in range(i+1):
            print("*", end='')
    for q in range(2*(n-i)-2):
            print(" ", end='')
    for r in range(i+1):
            print("*", end='')
          
    print()  