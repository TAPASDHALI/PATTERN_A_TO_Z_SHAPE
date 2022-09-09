#WAP TO PATTERN PROGRAM PRINTING STAR "*" IN V SHAPE?
print()
i = 0
j = 6
for row in range(4):
    for col in range(7):
        if row == col:
            print("*", end = "")
        elif row == i and col == j:
            print("*", end = "")
            i += 1
            j -= 1
        else:
            print(end = " ")
    print()
print()

#WAP TO PATTERN PROGRAM PRINTING STAR "*" IN V SHAPE?
print()
str1 = ""
i = 0
j = 6
for row in range(4):
    for col in range(7):
        if row == col:
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
