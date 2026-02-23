import random
my_list = random.randint(3,10)
lst = []
for i in range(my_list):
    lst.append(random.randint(1,10))
print(lst)
new_lst = [lst[0], lst[2], lst[-2]]
print(new_lst)