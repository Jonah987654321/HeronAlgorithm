def isnumber(zahl, type="int"):
    number = True
    try:
        if type == "float":
            float(zahl)
        elif type == "int":
            int(zahl)
    except ValueError:
        number = False
    return number

zahl = input("Enter the number from which the square root should be formed: ")
zahl_float = isnumber(zahl, "float")
while zahl_float is False or float(zahl) <= 0:
    print("Invalid input. Please insert number!")
    zahl = input("Enter the number from which the square root should be formed: ")
    zahl_float = isnumber(zahl, "float")
x = input("Enter accuracy (how often should the method be used?): ")
genauigkeit_int = isnumber(x, "int")
while genauigkeit_int is False or int(x) <= 0:
    print("Invalid input! Please insert natural number!")
    x = input("Enter accuracy (how often should the method be used?): ")
    genauigkeit_int = isnumber(x, "int")
x = int(x)
a = float(zahl)
print(f"Side length a: {a}")
zahl = float(zahl)
for r in range(1, x, 1):
    a_last = float(a)
    a = (a_last + (zahl / a_last)) / 2
    if a == a_last:
        break
    else:
        print(f"Side length a: {a}")
y = a*a
abweichung = abs(y-zahl)/zahl
abweichung = abweichung*100
abweichung = round(abweichung, 2)
print(f"\n\n\nThe computed approximation from the square root of {zahl} is {a}.")
print(f"NOTE: The square of the calculated approximation deviates by {abweichung}% from the entered number!")
