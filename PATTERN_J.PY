#WAP TO PATTERN PROGRAM PRINTING STAR "*" IN J SHAPE?
print()
for row in range(7):
    for col in range(5):
        if col == 2 or row == 0 or (row == 6 and (col != 3 and col != 4)):
            print("*", end = "")
        else:
            print(end = " ")
    print()
print()


#WAP TO PATTERN PROGRAM PRINTING STAR "*" IN J SHAPE?
str1 = ""
for row in range(7):
    for col in range(5):
        if col == 2 or row == 0 or (row == 6 and (col != 3 and col != 4)):
            str1 = str1 + "*"
        else:
            str1 = str1 + " "
    str1 = str1 + "\n"
print(str1)
print()

