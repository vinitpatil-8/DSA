s = "hello"
score = 0
for index, char in enumerate(s):
    if index>0:
        score = score + abs(ord(s[index-1]) - ord(char))
print(score)
    