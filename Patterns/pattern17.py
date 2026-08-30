n = int(input())
alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
for i in range(n):
    for a in range(n-i-1):
        print(" ", end=' ')
    for b in range(2*i+1):
        if b<=(2*i)/2:
            print(alphabets[b], end=' ')
        else:
            print(alphabets[(2*i)-b], end=' ')
    for c in range(n-i-1):
        print(" ", end=' ')
          
    print()    
        # space - n-i
        # Alphabets - 2*i+1
        # space - n-i