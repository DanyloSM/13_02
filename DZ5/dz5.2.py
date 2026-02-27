while True:
    a = float(input("Введіть перше число: "))
    b = float(input("Введіть други число: "))
    c = input("Введіть дію над цими числами(+,-,*,/): ")
    if c == "+":
        print("Результат: ", a + b)
    elif c == "-":
        print("Результат :", a - b)
    elif c == "*":
        print("Результат :", a * b)
    elif c == "/":
        if b == 0:
            print("Дільник не може дорівнювати нулю")
        else:
            print("Результат :", a / b)
    else:
        print("Незрозуміла дія")
    choice = input("Введіть 'yes' щоб продовжити: ").lower()
    if choice == "yes":
        continue
    else:
        print("Програма завершена.")
        break