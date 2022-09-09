#WAP TO PATTER PROGRAM PRINTING STAR "*" IN Q SHAPE?
for row in range(8):
    for col in range(5):
        if ((col == 0 or col == 4) and (row > 0 and row < 6)) or ((row == 0 or row == 6) and (col > 0 and col < 4)) or ((row == 7) and (col > 2 and col < 4)) or ((row == 5) and (col > 0 and col < 2)):
            print("*", end = "")
        else:
            print(end = " ")
    print()
print()


#WAP TO PATTER PROGRAM PRINTING STAR "*" IN Q SHAPE?
str1 = ""
for row in range(8):
    for col in range(5):
        if ((col == 0 or col == 4) and (row > 0 and row < 6)) or ((row == 0 or row == 6) and (col > 0 and col < 4)) or ((row == 7) and (col > 2 and col < 4)) or ((row == 5) and (col > 0 and col < 2)):
            str1 = str1 + "*"
        else:
            str1 = str1 + " "
    str1 = str1 + "\n"
print(str1)
print()
