#WAP TO PATTERN PROGRAM PRINTING STAR "*" IN P SHAPE?
print()
for row in range(7):
    for col in range(5):
        if col == 0 or (col == 4 and (row == 1 or row == 2)) or (row == 0 and (col != 4)) or row == 3 and col != 4:
            print("*", end = "")
        else:
            print(end = " ")
    print()
print()

#WAP TO PATTERN PROGRAM PRINTING STAR "*" IN P SHAPE?
str1 = ""
for row in range(7):
    for col in range(5):
        if col == 0 or (col == 4 and (row == 1 or row == 2)) or (row == 0 and (col != 4)) or row == 3 and col != 4:
            str1 = str1 + "*"
        else:
            str1 = str1 + " "
    str1 = str1 + "\n"
print(str1)
print()
