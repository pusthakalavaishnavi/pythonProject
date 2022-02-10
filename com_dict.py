# wap to print element as key in string and how many times element as repeated
# var = "python is very easy language and high level language"
# d={}
# # words = var.split()
# for i in var:
#     d[i] = var.count(i)
# print(d)

#char and ascii value pair

# var = "python is high level programing language"
# d = {}
# for i in var:
#     d[i] = ord(i)
# print(d)

#wap to flip key value pair in dict

var = {"k" : 12, "c" : 13, "g" : 45, "f" : 67, "j" : 78}
d = {}
# for key,value in var.items():
#     if value in d:
#         d[value].append(key)
#     else:
#         d[value] = [key]
# print("key : value")
# for i in d:
#     print(i, " :", d[i])

# comp_dict = {var[i] : i for i in var}

# comp_dict = {value : key for key,value in var.items()}
# print(comp_dict)

# or

# d = {"a": 1, "b":2}
# d1 = {}
# for key in d:
#     d1[d[key]] = key
# print(d1)

# p = ["python", 5, "how"]
# d = {}
# for index,i in enumerate(p):
#     if isinstance(i,str):
#         d[index] = i[::-1]
# print(d)
#
# s = "hello python language"
# d = {}
# words = s.split()
# for i in words:
#     d[i] = words.count(i)
# print(d)



#word and length pIR If the word is starting with vowel

# var = "python is starting in oxford university an every element brief"
# d = {}
# words = var.split()
# for i in words:
#     if i[0] in "aeiou":
#         d[i] = len(i)
# # print(d)
#
# comp_dict = {i : len(i) for i in words if i[0] in "aeiou"}
# print(d)

#index and word pair if word is of word reverse it

# var = "python is a high level programing language every"
# words = var.split()
# for i, in enumerate(words):
#     if i % 2 != 0:
#         i[::-1]


# item and count pair
s = "python"
# d = {}
# for i in s:
#     d[i] = s.count(i)

# com_dict = {i : s.count(i) for i in s}
# print(com_dict)

#char and its index pair

# var = "python is very easy language"
# d = {}
# words = var.split()

# for index,i in enumerate(words):
#     if i not in d:
#        d[i] = [index]
#     else:
#         d[i] += [index]
# print(d)

#wap to create a dict with charater and its count pair

# var = "python"
# d = {}
# for i in var:
#     d[i] = ord(i)
# print(d)

#wap to create a dict word and its length pair
#
# var = "python is very easy language"
# words = var.split()
# # d = {}
# # for i in words:
# #     d[i] = len(i)
# # print(d)
#
# com_dict = {i : len(i) for i in words}
# print(com_dict)

# cities = ["india", "china", "america", "canada"]
# population = [10, 20, 30, 40, 60, 69]
# # d={}
# # for i in range(len(cities)):
# #     d[cities[i]] = population[i]
# # print(d)
# from itertools import zip_longest
# c = zip_longest(cities, population)
# print(dict(c))

#flip keys and values in dic

# var = {"python":1, "is":2, "very" : "3"}
# d = {}
# for key in var:
#     value = var[key]
#     d[key] = value
# print(d)




var = "hello is python every"
words = var.split()
d = {}
for i in words:
    if len(i)%2==0:
        d[i] = words.count(i)
print(d)












