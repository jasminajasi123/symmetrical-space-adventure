# exercise lambda expressions

my_list = [1,2,6]
new_list = list(map(lambda num: num ** 2, my_list))
print(new_list)

a = [(10,2),(3,5),(-9,7)]
a.sort(key = lambda x: x[1])
print(a)