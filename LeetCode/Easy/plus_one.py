digits = input()
inputInt = int("".join(map(str, digits))) + 1
print([int(x) for x in str(inputInt)])