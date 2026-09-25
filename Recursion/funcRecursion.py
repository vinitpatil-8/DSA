# Reverse a list by recursion by two pointers
print("Reverse a list by recursion by two pointers")
arr = [1, 2, 7, 8, 9, 4, 0, 6]
def reverse(a, b):
    if a>=b:
        return
    arr[a], arr[b] = arr[b], arr[a]
    reverse(a+1, b-1)
reverse(0, len(arr)-1)
print(arr)

# Reverse a list by recursion by single pointer
print("Reverse a list by recursion by single pointer")
arr1 = [1, 2, 3, 4, 5, 6, 7, 8]
def reverse(i):
    if i>=(len(arr1)-1)/2:
        return
    arr1[i], arr1[len(arr1)-i-1] = arr1[len(arr1)-i-1], arr1[i]
    reverse(i+1)
reverse(0)
print(arr1)

# Check if given string is a palindrome - single pointer
print("Check if given string is a palindrome")
str1 = "madam"
def checkPalindrome(a, s):
    n = len(s)
    if a>=(n/2):
        print("palindrome")
        return True
    if s[a] != s[n-a-1]:
        print("not palindrome")
        return False
    checkPalindrome(a+1, s)
checkPalindrome(0, str1)

# Fibonacci Number
# TODO : create a whole diagram on excalidraw
print("Fibonacci Number")
def fibonacci(n):
    if n<=1:
        return n
    last = fibonacci(n-1)
    slast = fibonacci(n-2)
    return last+slast
print(fibonacci(6))