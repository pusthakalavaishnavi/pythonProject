# path = r"C:\Users\user\PycharmProjects\pythonProject\PythonPractice\file handiling\sample.txt"
# with open(path) as file:
#     for line in file:
#         print(line)


# path = r"C:\Users\user\PycharmProjects\pythonProject\PythonPractice\file handiling\sample.txt"
# with open(path) as file:
#     count = 0
#     for line in file:
#         count += 1
#     print(f"the count of lines is {count}")


# path = r"C:\Users\user\PycharmProjects\pythonProject\PythonPractice\file handiling\sample.txt"
# with open(path) as file:
#     count = 0
#     for line in file:
#         count+=1
#         print(count,line)

# path = r"C:\Users\user\PycharmProjects\pythonProject\PythonPractice\file handiling\sample.txt"
# with open(path) as file:
#     for line in reversed(list(file)):
#         print(line)

# path = r"C:\Users\user\PycharmProjects\pythonProject\PythonPractice\file handiling\sample.txt"
# with open(path) as file:
#     count = 0
#     for line in file:
#        for char in line:
#            if char == " ":
#                count+=1
#     print(count)

# path = r"C:\Users\user\PycharmProjects\pythonProject\PythonPractice\file handiling\sample.txt"
# with open(path) as file:
#     d = {}
#     count = 0
#     for line in file:
#         words = line.split()
#         for word in words:
#           if word not in d:
#               d[word] = 1
#           d[word]+=1
#
#     print(d)

path = r"C:\Users\user\PycharmProjects\pythonProject\PythonPractice\file handiling\sample.txt"
# from collections import defaultdict
# with open(path) as file:
#     d=defaultdict(int)
#     for i in file:
#         for word in i.split():
#             d[word] += 1
#     print(d)

path = r"C:\Users\user\PycharmProjects\pythonProject\PythonPractice\file handiling\sample.txt"
with open(path) as file:
    for line in file:
        print(len(line))











