n = int(input())
alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
for i in range(1, n+1):
    for j in range(1, n+1):
        if j<=i:
            if j==1:
                start = n-i-j+1
                print(alphabets[start], end='')
                
            else:
                start=start+1
                print(alphabets[start], end='')
    print()      