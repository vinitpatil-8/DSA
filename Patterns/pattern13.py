n = int(input())
output = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        if j<=i:
            output += 1
            print(output, end=' ')
    print()