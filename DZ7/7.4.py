def common_elements():
    first_1 = []
    first_2 = []
    first = range(100)
    for num in first:
        if num % 3 == 0:
            first_1.append(num)
        if num % 5 == 0:
            first_2.append(num)
    result = set(first_1)&set(first_2)
    return result


assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print("OK")
