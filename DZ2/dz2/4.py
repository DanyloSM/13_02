price = float(input("Enter price: "))
discount = float(input("Enter discount(%): "))
x = price - ((discount * price) / 100)
print("New price: ", x)
