#WAP TO PATTERN PROGRAM PRINTING STAR "*" IN W SHAPE?
print()
i = 0
j = 3
for row in range(4):
    for col in range(7):
        if col == 0 or col == 6 or (col == 4 and row == 1) or (col == 5 and row == 2):
            print("*", end = "")
        elif row == i and col == j:
            print("*", end = "")
            i += 1
            j -= 1
        else:
            print(end = " ")
    print()
print()

#WAP TO PATTERN PROGRAM PRINTING STAR "*" IN W SHAPE?
print()
str1 = ""
i = 0
j = 3
for row in range(4):
    for col in range(7):
        if col == 0 or col == 6 or (col == 4 and row == 1) or (col == 5 and row == 2):
            str1 += "*"
        elif row == i and col == j:
            str1 += "*"
            i += 1
            j -= 1
        else:
            str1 += " "
    str1 += "\n"
print(str1)
print()