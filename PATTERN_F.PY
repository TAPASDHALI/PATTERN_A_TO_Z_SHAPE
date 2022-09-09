# WAP TO PATTERN PROGRAM PRINTING STAR "*" IN F SHAPE?
for row in range(7):
    for col in range(5):
        if col == 0 or row == 0 or row == 3:
            print("*", end="")
        else:
            print(end = " ")
    print()
print()

# WAP TO PATTERN PROGRAM PRINTING STAR "*" IN F SHAPE?
str1 = ""
for row in range(7):
    for col in range(5):
        if col == 0 or row == 0 or row == 3:
            str1 = str1 + "*"
        else:
            str1 = str1 + " "
    str1 = str1 + "\n"
print(str1)