#WAP TO PATTERN PROGRAM PRINTING STAR "*" IN L SHAPE?
print()
for row in range(7):
    for col in range(5):
        if col == 0 or row == 6:
            print("*", end = "")
        else:
            print(end = " ")
    print()
print()


#WAP TO PATTERN PROGRAM PRINTING STAR "*" IN L SHAPE?
str1 = ""
print()
for row in range(7):
    for col in range(5):
        if col == 0 or row == 6:
            str1 = str1 + "*"
        else:
            str1 = str1 + " "
    str1 = str1 + "\n"
print(str1)
print()
