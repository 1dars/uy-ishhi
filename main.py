# 1-misol
# def integer_boolean(lst):
#     a = []
#     i = 0
#     while i < len(lst):
#         x = lst[i]
#         i += 1
#         if x == "1":
#             b = x.replace("1", str("tog'ri"))
#             a.append(b)
#         else:
#             c = x.replace("0", str("xato"))
#             a.append(c)
#     return a
# 3 misol
# def calc(input_string):
#     vowels = "aeiou"
#     i = 0
#     b = ""
#     while i < len(input_string):
#         a = input_string[i]
#         if a not in vowels:
#             b = b + a
#         i += 1
#     return b
# print(calc("zor"))
# 4 misol
# def calc(lst):
#     i = 0
#     list = []
#     while i < len(lst):
#         a = lst[i]
#         if a == '1':
#             print("tog'ri")
#         else:
#             print("xatto")
#         i += 1
#     return i
# print(calc("1"))
# 6 misol
# def calc(lst):
#     a = ""
#     i = 0
#     while i < len(lst):
#         x = lst[i]
#         i += 1
#         if x.isdigit():
#             a += x
#     return a[0:1]
# print(calc("alooooo"))
# 8 misol
# def calc(lst):
#     i = 0
#     while i < len(lst):
#         a = lst[i]
#         b = a.replace("a","i")
#         i += 1
#         print(b)
# print(calc("shaptoli"))
