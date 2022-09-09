# WAP TO PATTER PRINTING PROGRAM PRINTING STAR "*" IN M SHAPE?
print()
for row in range(7):
    for col in range(7):
        if col == 0 or col == 6 or ((row == col) and (col > 0 and col < 4)) or (row == 1 and col == 5) or (row == 2 and col == 4):
            print("*", end = "")
        else:
            print(end = " ")
    print()
print()
# WAP TO PATTER PRINTING PROGRAM PRINTING STAR "*" IN M SHAPE?
str1 = ""
print()
for row in range(7):
    for col in range(7):
        if col == 0 or col == 6 or ((row == col) and (col > 0 and col < 4)) or (row == 1 and col == 5) or (row == 2 and col == 4):
            str1 = str1 + "*"
        else:
            str1 = str1 + " "
    str1 = str1 + "\n"
print(str1)
print()