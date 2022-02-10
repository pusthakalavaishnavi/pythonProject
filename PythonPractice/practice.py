"""return last digit of an intiger"""

# def func_(num):
#    return num%10
#
# print(func_(155))

# def func_(last,n):
#     return last[-n]
#
# print(func_("hello",2))

# def fun_(num):
#     for i in range(num):
#         num+=1
#         print(i)
# fun_(10)

"""dictionary of word and its count pair using function"""
# sentence = "it is a very good book and reading is a good habit"
# def dict_():
#     d={}
#     for i in sentence:
#         words = i.split()
#         for words in i:
#             d[words] = i.count(d[words])
#     return d

def rec(strng):
    print(strng)
    return rec(strng[1::])

















