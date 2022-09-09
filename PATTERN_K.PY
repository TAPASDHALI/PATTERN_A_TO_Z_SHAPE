#WAP TO PATTERN PROGRAM PRINTING STAR "*" IN K SHAPE?
print()
i = 0 
j = 4
for row in range(7):
    for col in range(5):
        if col == 0 or (row == col + 2 and col > 1):
            print("*", end = "")
        elif (row == i and col == j):
            print("*", end = "")
            i += 1
            j -= 1
        else:
            print(end = " ")
    print()
print()

#WAP TO PATTERN PROGRAM PRINTING STAR "*" IN K SHAPE?
print()
str1 = ""
i = 0 
j = 4
for row in range(7):
    for col in range(5):
        if col == 0 or (row == col + 2 and col > 1):
            str1 = str1 + "*"
        elif (row == i and col == j):
            str1 = str1 + "*"
            i += 1
            j -= 1
        else:
            str1 = str1 + " "
    str1 = str1 + "\n"
print(str1)
print()