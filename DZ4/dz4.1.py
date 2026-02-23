
#my_list = [0, 1, 0, 12, 3] #-> [1, 12, 3, 0, 0]
#my_list = [0] #-> [0]
#my_list = [1, 0, 13, 0, 0, 0, 5] #-> [1, 13, 5, 0, 0, 0, 0]
my_list = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0] #-> [9, 7, 31, 45, 45, 45, 96, 0, 0, 0, 0, 0, 0, 0]
no_zero = []
zero = []
for num in my_list:
    if num == 0:
        zero.append(num)
    else:
        no_zero.append(num)
my_list = no_zero + zero
print(my_list)



