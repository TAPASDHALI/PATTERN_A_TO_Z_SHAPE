# WAP TO PROGRAM PRINTING STAR "*" IN G SHAPE?
for row in range(7):
    for col in range(6):
        if ((col == 0) or (col == 4) and (row != 1 and row != 2)) or (((row == 0) and (col!= 5)) or ((row == 3)and (col != 1 and col!= 2)) or ((row == 6) and (col != 5))):
            print("*", end = "")
        else:
            print(end =" ")
    print()
print()


# WAP TO PROGRAM PRINTING STAR "*" IN G SHAPE?
str1 = ""
for row in range(7):
    for col in range(6):
        if ((col == 0) or (col == 4) and (row != 1 and row != 2)) or (((row == 0) and (col!= 5)) or ((row == 3)and (col != 1 and col!= 2)) or ((row == 6) and (col != 5))):
            str1 = str1 + "*"
        else:
            str1 = str1 + " "
    str1 = str1 + "\n"
print(str1)