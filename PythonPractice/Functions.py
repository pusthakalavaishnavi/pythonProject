# def fibo(num):
#     a=0
#     b=1
#     while a <= num:
#         if a == num:
#             return f"{num} is fibo"
#         c=a+b
#         a = b
#         b = c
#     return f"{num} is not fibo"
#
# print(fibo(5))

#wap the take variable number of input that return length of iterable
# d={ }
# def iterable_len(*arg):
#     for i in arg:
#         if isinstance(i,(set,list,tuple,dict,str)):
#             d[i]=len(i)
#             print(d)
# (iterable_len(1,"hello",(1,2,3),[1,2]))

"""returning multiple value"""

# def func_(a,b):
#     print(a*b)
#     return a,b
# res =func_(10,20)
# print(res)

"""example"""

def func_(a):
    return a
print(func_(41))

"""default function"""

# def even(end,start=0):
#     list_=[]
#     for items in range(start,end+1):
#         if items %2==0:
#            list_.append(items)
#     return list_
#
# new_list = even(50,5)
# print(new_list)

"""example"""
# def add_(a,b):
#     return a+b
# print(add_(10,20))

"""examples"""

# def fun_(a,b,c=0):
#     return a+b+c
# print(fun_(10,20))

# x=50
# def add_(a,b=x):
#     print(a+b)
# x=50
# add_(10)

# def add_(a:str,b:str):
#     print(a+b)
# print(add_(10,20))
# print(add_("a","b"))

"""printing result in the function body"""

# def fun_(v1,v2):
#     a=v1
#     b=v2
#     c=a+b
#     return c
# print(fun_(10,30))

"""print series of n numbers """

# def fun_(a):
#     for i in range(1,a+1):
#         print(i)
# fun_(15)

"""prime number"""
def is_prime(num):

    for i in range(2, num):
        if num % i == 0:
            return f"{num} is not prime"
    return f"{num} is a prime"

print(is_prime(4))
print(is_prime(6))

# def last_num(num):
#     # return num%10
#     return num[-1]
# print(last_num("string"))

# def tail(sequence, n):
#     return sequence[-n:]
#
# print(tail("string", 5))
# print(tail("hello", 4))

"""square"""
def is_perfect_sqaure(num):
    sq= i*i ==num
    return num
is_perfect_sqaure(25)
print(is_perfect_sqaure)

















