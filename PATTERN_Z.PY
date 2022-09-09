#WAP TO PATTERN PROGRAM PRINTING STAR "*" IN Z SHAPE?
print()
i = 1 
j = 4
for row in range(6):
    for col in range(6):
        if row == 0 or row == 5:
            print("*", end = "")
        elif row == i and col == j:
            print("*", end = "")
            i += 1
            j -= 1
        else:
            print(end = " ")
    print()
print()

#WAP TO PATTERN PROGRAM PRINTING STAR "*" IN Z SHAPE?
print()
str1 = ""
i = 1 
j = 4
for row in range(6):
    for col in range(6):
        if row == 0 or row == 5:
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
