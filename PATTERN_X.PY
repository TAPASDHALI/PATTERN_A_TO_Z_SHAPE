#WAP TO PATTERN PROGRAM PRINTING STAR "*" IN X SHAPE?
print()
i = 0
j = 4
for row in range(5):
    for col in range(5):
        if row == i and col == j:
            print("*", end = "")
            i += 1
            j -= 1
        elif row == col:
            print("*", end = "")
        else:
            print(end = " ")
    print()
print()


#WAP TO PATTERN PROGRAM PRINTING STAR "*" IN X SHAPE?
print()
str1 = ""
i = 0
j = 4
for row in range(5):
    for col in range(5):
        if row == i and col == j:
            str1 += "*"
            i += 1
            j -= 1
        elif row == col:
            str1 += "*"
        else:
            str1 += " "
    str1 += "\n"
print(str1)
print()
