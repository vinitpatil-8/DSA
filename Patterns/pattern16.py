n = int(input())
alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
for i in range(1, n+1):
    for j in range(1, n+1):
        if j<=i:
            print(alphabets[i-1], end=' ')
    print()