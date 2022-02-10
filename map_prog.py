# num = [10, 20, 30, 40]
# def power(iteams):
#     index,num = iteams
#     num = num ** index
#
# res = map(power,enumerate(num  ))


#list of list elements
l = ["p", "y", "t", "h", "o", "n"]
# def list_(i):
#     return i

# res = list(map(set,l))
# print(res)

# wap to print lambda exp to check if the given exp is even or odd

# var = lambda num : "even" if num % 2 == 0 else "odd"
# res =var(3)
# print(str(res))

# wap lambda exp mul of two numbers

# var = lambda num1,num2: num1 * num2
# res = var(1,2)
# print(int(res))

# wap to check pallindrom

# list = "pin"
# palindrom = lambda a : a if a == a[::-1] else "not"
# for i in list:
#     print(palindrom(list))

# list = [10,20,25,30,35]
# def even_odd(list):
#         if i%2==0:
#             return even
#
# res = map(even_odd(),list)
# print(list(res))

a = map(lambda x: x%2 == 0, a)
print(a(10))







