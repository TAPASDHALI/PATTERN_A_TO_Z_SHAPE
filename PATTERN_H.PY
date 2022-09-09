#WAP TO PATTERN PROGRAM PRINTING STAR "*" IN H SHAPE?
print()
for row in range(7):
    for col in range(6):
        if col == 0 or col == 5 or row == 3:
            print("*", end = "")
        else:
            print(end = " ")
    print()
print()

#WAP TO PATTERN PROGRAM PRINTING STAR "*" IN H SHAPE?
str1 = ""
print()
for row in range(7):
    for col in range(6):
        if col == 0 or col == 5 or row == 3:
            str1 = str1 + "*"
        else:
            str1 = str1 + " "
    str1 = str1 + "\n"
print(str1)
print()
