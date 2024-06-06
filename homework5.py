immutable_var = 1, 2, 3, False, 'String', 3.6
print(immutable_var)
#immutable_var[0]=5
#print(immutable_var)
#кортеж нельзя изменить, так как он неизменяем.
mutable_list = ([1, 2, 3], 6, True)
mutable_list[0][1] = 7
print(mutable_list)

