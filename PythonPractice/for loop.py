# l=[1,2,3,4,5]
# for x in l:
#     print(x)

# l=[1,2,3,4,5]
# lis_comp=[i for i in l]
# print(lis_comp)

s="hello"
for x in range(len(s)):
    print(s[x], x)
#
#
# for x in range(1,len(s),2):
#     print(s[x])


# l=[1,2,3,4,5,6,7,8,9,10]
# for i in range(len(l)):
#      if i%2==0:
#          continue
#          print("even",i,l[i])
#      else:
#         print("odd",i)


# for i in range(0,30):
#     print(i)


# s = "python"
# for i in range(len(s)):
#     print(ord(s[i]))


# s = " a"
# for i in range(len(s)):
#     print(chr(ord(s[i])))

# s="hai good morning"
# d= {""}
# # for i in s:
# #     if "a" <=i<="z" and "AaEeIiOoUu":
# #         d+= chr(ord(i)-32)
# #     elif i in "aAeEiIoOuU" and "A"<=i<="Z":
# #         d+=chr(ord(i)+32)
# #     else:
# #         d+=i
# # print(d)
#
# words=s.split()
# for word in words:
#     if word[0] in "aeiouAEIOU":
#         d[word]=len(word)
# print(d)

# s="abcd"
# d={}
# for i in s:
#     d[i]=ord(i)
#     print(d)

# s="my name is anu iam studying oracle in university"
# l=[ ]
# words=s.split()
# for word in words:
#     if word[0] in "aeiouAEIOU":
#         a = l.append((word))
#         print(word)
# print(l)

# list=[1,2,3,4,5,6,7,8,9,10]
# list_comp=[i for i in list if i%2==0]
# print(list_comp)

# s={0,1,2,3,4,5,6,7,8,10}
# set_comp={i for i in s if i%2==0}
# print(set_comp)

d=[0,1,2,3,4,5,6,7,8,9,10]
dict_comp={i:i for i in d if i%2!=0}
print(dict_comp)





