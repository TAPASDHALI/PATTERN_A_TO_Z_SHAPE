# WAP TO PATTER PROGRAM PRINTING STRA "*" IN U SHAPE?
print()
for row in range(6):
    for col in range(6):
        if col == 0 and (row < 5) or col == 5 and ( row < 5) or row == 5 and (col > 0 and col < 5):
            print("*", end = "")
        else:
            print(end = " ")
    print()
print()

# WAP TO PATTER PROGRAM PRINTING STRA "*" IN U SHAPE?
print()
str1 = ""
for row in range(6):
    for col in range(6):
        if col == 0 and (row < 5) or col == 5 and ( row < 5) or row == 5 and (col > 0 and col < 5):
            str1 += "*"
        else:
            str1 += " "
    str1 += "\n"
print(str1)
