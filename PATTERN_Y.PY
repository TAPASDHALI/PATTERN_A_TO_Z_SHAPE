#WAP TO PATTERN PROGRAM PRINTING STAR "*" IN Y SHAPE?
print()
for row in range(5):
    for col in range(5):
        if (col == 2 and row > 1) or (row == col and col < 2) or (row == 0 and col == 4) or (row == 1 and col == 3):
            print("*", end = "")
        else:
            print(end = " ")
    print()
print()

#WAP TO PATTERN PROGRAM PRINTING STAR "*" IN Y SHAPE?
print()
str1 = ""
for row in range(5):
    for col in range(5):
        if (col == 2 and row > 1) or (row == col and col < 2) or (row == 0 and col == 4) or (row == 1 and col == 3):
            str1 += "*"
        else:
            str1 += " "
    str1 += "\n"
print(str1)
print()