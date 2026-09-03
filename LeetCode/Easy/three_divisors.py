n = int(input())
root = int(n ** 0.5)
        
# Check if n is a perfect square
if root * root != n:
    print(False)
            
# Check if root is prime
if root < 2:
    print(False)
            
for i in range(2, int(root ** 0.5) + 1):
    if root % i == 0:
        print(False)                
    print(True)