str = input()

for i in range(len(str)):
    if i%2 == 0:
        print(str[i], end="")
    else:
        print(ord(str[i]), end="")
