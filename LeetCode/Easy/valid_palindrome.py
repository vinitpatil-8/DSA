s = input()
cleaned = "".join(c for c in s if c.isalnum() and c.isascii()).lower()
reversed_str = cleaned[::-1]
if reversed_str == cleaned:
    print(True)
else:
    print(False)