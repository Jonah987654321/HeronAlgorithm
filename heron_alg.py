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

num = input("Enter the number from which the square root should be formed: ")
num_float = isnumber(num, "float")
while num_float is False or float(num) <= 0:
    print("Invalid input. Please insert number!")
    num = input("Enter the number from which the square root should be formed: ")
    num_float = isnumber(num, "float")
x = input("Enter accuracy (how often should the method be used?): ")
accuracy_int = isnumber(x, "int")
while accuracy_int is False or int(x) <= 0:
    print("Invalid input! Please insert natural number!")
    x = input("Enter accuracy (how often should the method be used?): ")
    accuracy = isnumber(x, "int")
x = int(x)
a = float(num)
num = float(num)
for r in range(1, x, 1):
    a_last = float(a)
    a = (a_last + (zahl / a_last)) / 2
    if a == a_last:
        break
y = a*a
approximation = abs(y-num)/num
approximation = approximation*100
approximation = round(approximation, 2)
print(f"\n\n\nThe computed approximation from the square root of {num} is {a}.")
print(f"NOTE: The square of the calculated approximation deviates by {approximation}% from the entered number!")
