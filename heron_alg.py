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

zahl = input("Zahl eingeben, aus der die Wurzel gezogen werden soll: ")
zahl_float = isnumber(zahl, "float")
while zahl_float is False or float(zahl) <= 0:
    print("Ungültige Eingabe. Bitte Zahl eingeben!")
    zahl = input("Zahl eingeben, aus der die Wurzel gezogen werden soll: ")
    zahl_float = isnumber(zahl, "float")
x = input("Genauigkeit eingeben (wie oft soll das Verfahren angewendet werden?): ")
genauigkeit_int = isnumber(x, "int")
while genauigkeit_int is False or int(x) <= 0:
    print("Ungültige Eingabe. Bitte natürliche Zahl eingeben!")
    x = input("Genauigkeit eingeben (wie oft soll das Verfahren angewendet werden?): ")
    genauigkeit_int = isnumber(x, "int")
x = int(x)
a = float(zahl)
print(f"Seitenlänge a: {a}")
zahl = float(zahl)
for r in range(1, x, 1):
    a_last = float(a)
    a = (a_last + (zahl / a_last)) / 2
    if a == a_last:
        break
    else:
        print(f"Seitenlänge a: {a}")
y = a*a
abweichung = abs(y-zahl)/zahl
abweichung = abweichung*100
abweichung = round(abweichung, 2)
print(f"\n\n\nDie berechnete Annäherung von der Wurzel aus {zahl} ist {a}.")
print(f"HINWEIS: Das Quadrat der berechnete Annäherung weicht um {abweichung}% von der eingegebenen Zahl ab!")