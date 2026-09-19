# Reverse a list by recursion
arr = [1, 2, 7, 8, 9, 4, 0, 6]
def reverse(a, b):
    if a>=b:
        return
    arr[a], arr[b] = arr[b], arr[a]
    reverse(a+1, b-1)
reverse(0, len(arr)-1)
print(arr)