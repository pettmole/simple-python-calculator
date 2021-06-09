# This is a simple calculator script not much else lol
def math():
    print("select your option a for addition s for subtraction m for multiplication d for division")
    option = str(input())
    var1 = float(input())
    if option == "a":
        print("+")
    if option == "s":
        print("-")
    if option == "m":
        print("x")
    if option == "d":
        print("÷")
    var2 = float(input())
    sum = var1 + var2
    difference = var1 - var2
    product = var1 * var2
    quotient = var1 / var2
    if option == "a":
        print(sum)
    if option == "s":
        print(difference)
    if option == "m":
        print(product)
    if option == "d":
        print(quotient)


print("another question?")
yesno = input()
if yesno == "yes":
    math()
