#WAP TO PATTERN PROGRAM PRINTING STAR "*" IN I SHAPE?
for row in range(7):
    for col in range(5):
        if col == 2 or ((row == 0) and (col > 0 and col < 4) or (row == 6)):
            print("*", end = "")
        else:
            print(end = " ")
    print()
print()


#WAP TO PATTERN PROGRAM PRINTING STAR "*" IN I SHAPE?
str1 = ""
for row in range(7):
    for col in range(5):
        if col == 2 or ((row == 0) and (col > 0 and col < 4) or (row == 6)):
            str1 = str1 + "*"
        else:
            str1 = str1 + " "
    str1 = str1 + "\n"
print(str1)
print()
