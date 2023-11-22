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

a = float(num)
num = float(num)
a_last = float(a)
a = (a_last + (num / a_last)) / 2
while a != a_last:
    a_last = float(a)
    a = (a_last + (num / a_last)) / 2

print(f"\n\n\nThe computed approximation from the square root of {num} is {a}")
