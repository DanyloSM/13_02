number = int(input("Enter a number:"))
while number > 9:
    product = 1
    for d in str(number):
        product *= int(d)
    number = product
print(number)