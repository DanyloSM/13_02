#my_list = [1, 3, 5] #=> 30
#my_list = [6] #=> 36
my_list = [] #=> 0
if len(my_list) == 0:
    result = 0
else:
    sum_nums =0
    for num in range(0, len(my_list), 2):
        sum_nums += my_list[num]
    result = sum_nums * my_list[-1]
print(result)


