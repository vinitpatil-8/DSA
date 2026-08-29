n = int(input())
alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
for i in range(n):
    push = 0
    for j in range(n-i):
        print(alphabets[push], end='')
        push+=1
    print()