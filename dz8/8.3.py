def find_unique_value(some_list):
    count = {}
    for i in some_list:
        count[i] = count.get(i, 0) + 1
    for key in count:
        if count[key] == 1:
            return key
assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
print("ОК")
