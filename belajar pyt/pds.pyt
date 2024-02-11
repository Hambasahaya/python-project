# # print(type(9.2))
# # print(type("9"))
# # print(type([7, 8, 9]))
# # print(type({'A': 7, "B": 8, "C": 9}))


# class orang:
#     nama = 'miftah'
#     umur = 20


# # neworang = orang()
# # print(type(neworang))
# obj = type('A', (object,), dict(nama="salsa", umur=23))
# print(type(obj))
# print(vars(obj))


# obj2 = type('b', (orang,), dict(nama="miftah", umur=20))
# print(type(obj2))
# print(vars(obj2))
# from functools import reduce


# def add_num(a, b):
#     return a+b


# a = [1, 2, 6, 20]
# print(reduce(add_num, a))


# class Mtk():
#     def perkalian(q, b):
#         return q*b


# Mtk.perkalian = staticmethod(Mtk.perkalian)
# print("x*y hasilnya adalah:", Mtk.perkalian(2, 9))
# string = "DQlab adalah kurusus data science di indonesia"
# string2 = string.split()
# print(string)
# print(string2)
# eks = '(1+2)**3'
# print(eval(eks))
print(round(10))
print(round(3.1413, 2))
print(round(3.1417, 2))
print(round(5.5))
