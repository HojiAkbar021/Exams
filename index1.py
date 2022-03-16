#Написать функцию, которая сперва принимает имя игрока, затем очки ... и выводит информацию

# Написать функцию, которая принимает много цифр (...) и умножает их на 2.

# Написать функцию, которая принимает слова отдельно (...), вам нужно их итерировать и вывести построчно. Input: func('Hello', 'Welcome', 'to', 'GeeksforGeeks') Output: 
# Hello 
# Welcome
# to
# GeeksforGeeks

# Написать функцию, которая принимает аргумент owner, и аргумент cars в виде kwargs

# Написать функцию, которая принимает kwargs, в аргументах мы передаем firstname = “Muntasir”, lastname = “IT”, age = 30, country = “USA”, email = “mun@gmail.com”, phone = “0987654”. Все это вывести построчно

# Написать функцию, которая принимает kwargs в мы туда передаем страны, то есть в key английское название, а в value русское название 

# Написать функцию lexus, которая принимает kwargs,  в аргументах передаем его технические характеристики. Все это вывести.

# Есть обычная функция 
# def hello(x):
#     return x * x
# Превратите данную функцию в lambda функцию 

# Есть список name = [“Kuma”, “Nurtilek”, “Zina”, “Edzen”, “Kuma”, “Aitenur”, “Zina” ]
#   Уберите дубликаты с данного листа с помощью lambda функций

# Есть список numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Выведите с помощью lambda функции чётные числа с списка

# names = [“azat”, “zina”, “kuma”, “anna”, “sas”] 
# Вывести с помощью lambda функции имена палиндромы

# def points(name, *point):
#      print(name, point)
# points("Akbar", 10, 15, 20)

# def numbers(*num):
#      for i in num:
#           print(i*2)
# numbers(5, 10, 20)

# def owner1(owner, **cars):
#      print(owner, cars)
# owner1("mashina", bmw = "5.0", merc = "4.6")

# def Itrun(**kwargs):
#      print(kwargs)
# Itrun(firstname = "Muntasir", lastname = "IT", age = "30", country = "USA", email = "mun@gmail.com", phone = "0987654")

# def contry(**kwargs):
#      print(kwargs)
# contry(amerika = "америка", russia = "россия")

# def lexsus(**option):
#      print(option)
# lexsus(obyom = "2.6", kuzov = "kupe")

# nums = lambda x:x*x
# print(nums(6))

# name = ["kuma", "Akbar", "Muntasir","kuma"]
# name1 =  lambda x:set(x)
# print(name1(name))

# print(list(filter(lambda x : x%2 == 0,[1,2,3,4,5,6,7,8,9,10])))

# print(list(filter(lambda x : x == x[::-1],["azat", "zina", "kuma", "anna", "sas"])))