# У вас есть словарь студентов IT RUN
students = [
    {'name': 'Mark', 'age': 18, 'course': 'java1', 'gender': 'Male'},
    {'name': 'John', 'age': 15, 'course': 'python', 'gender': 'Male'},
    {'name': 'Andrew', 'age': 20, 'course': 'javascript', 'gender': 'Male'},
    {'name': 'Marcus', 'age': 25, 'course': 'java1', 'gender': 'Male'},
    {'name': 'Agnes', 'age': 40, 'course': 'python', 'gender': 'Female'},
    {'name': 'Doe', 'age': 42, 'course': 'java1', 'gender': 'Male'},
    {'name': 'Michael', 'age': 17, 'course': 'javascript', 'gender': 'Male'},
    {'name': 'Jennifer', 'age': 16, 'course': 'java1', 'gender': 'Female'},
    {'name': 'Angela', 'age': 16, 'course': 'python', 'gender': 'Female'},
    {'name': 'Eniston', 'age': 34, 'course': 'java1', 'gender': 'Male'},
    {'name': 'Albert', 'age': 33, 'course': 'javascript', 'gender': 'Male'},
    {'name': 'Nash', 'age': 28, 'course': 'python', 'gender': 'Male'},
    {'name': 'Nicolas', 'age': 19, 'course': 'java1', 'gender': 'Male'},
    {'name': 'Alex', 'age': 21, 'course': 'java1', 'gender': 'Male'},
    {'name': 'Martin', 'age': 22, 'course': 'python', 'gender': 'Male'},
    {'name': 'Gloria', 'age': 23, 'course': 'java1', 'gender': 'Female'},
    {'name': 'Mikkel', 'age': 24, 'course': 'python', 'gender': 'Male'},
    {'name': 'Susann', 'age': 25, 'course': 'javascript', 'gender': 'Female'},
    {'name': 'Steve', 'age': 26, 'course': 'python', 'gender': 'Male'},
    {'name': 'Mark', 'age': 18, 'course': 'java1', 'gender': 'Male'},
    {'name': 'Johnathan', 'age': 15, 'course': 'python', 'gender': 'Male'},
    {'name': 'Aidin', 'age': 20, 'course': 'javascript', 'gender': 'Male'},
    {'name': 'Mirbek', 'age': 25, 'course': 'java1', 'gender': 'Male'},
    {'name': 'Aidana', 'age': 40, 'course': 'python', 'gender': 'Female'},
    {'name': 'Atay', 'age': 42, 'course': 'java1', 'gender': 'Male'},
    {'name': 'Chyngyz', 'age': 17, 'course': 'javascript', 'gender': 'Male'},
    {'name': 'Aigerim', 'age': 16, 'course': 'java1', 'gender': 'Female'},
    {'name': 'Jyldyz', 'age': 16, 'course': 'python', 'gender': 'Female'},
    {'name': 'Emir', 'age': 34, 'course': 'java1', 'gender': 'Male'},
    {'name': 'Emirlan', 'age': 12, 'course': 'javascript', 'gender': 'Male'},
    {'name': 'Nursultan', 'age': 13, 'course': 'python', 'gender': 'Male'},
    {'name': 'Aliaskar', 'age': 19, 'course': 'java1', 'gender': 'Male'},
    {'name': 'Aktan', 'age': 21, 'course': 'java1', 'gender': 'Male'},
    {'name': 'Adyl', 'age': 14, 'course': 'python', 'gender': 'Male'},
    {'name': 'Gloria', 'age': 23, 'course': 'java1', 'gender': 'Female'},
    {'name': 'Janyl', 'age': 16, 'course': 'python', 'gender': 'Female'},
    {'name': 'Meerim', 'age': 12, 'course': 'javascript', 'gender': 'Female'},
    {'name': 'Sultan', 'age': 13, 'course': 'python', 'gender': 'Male'},
]
# 1) высните процентное соотношение мужского пола и женского.
# 2) выведите всех студентов с курса python
# 3) уберите дубликаты
# 4) выведите студентов, которые старше 30 и найдите процент их количества относительно других
# 5) отсортируйте студентов по:имени курсу полу возрасту
# 6) все студенты курса  javascript  перешли на курс  python.  Как вы поменяете это в словаре ? Напишите код
# 7) Добавьте по 5 новых студентов на курсы  java  и  python
# 8)  Отчислите всех студентов младше 15 лет
# # 1)
# lst = []
# for i in students:
#     lst.append(i['gender'])
# all1 = lst.count('Male')
# all2 = lst.count('Female')
# male = all1 / (all1+all2)*100
# female = all2 / (all1+all2)*100
# print(f"мужчин:{round(male,2)}%, женшин:{round(female, 2)}%")
# # 2)
# for i in students:
#     if i['course'] == 'python':
#         print(i ['name'])
# # 3)
# set1 = set()
# for i in students:
#     for k, v in i.items():
#         if k == 'name':
#             set1.add(v)
# names = (list(set1))
# set2 = list(set())
# for x in names:
#     for y in students:
#         if y['name'] in x:
#             set2.append(y)
# print(set2)
# # 4)
# lst1 = 0
# for i in students:
#     if i['age'] > 30:
#         lst1 += 1
#         print(lst1, i['name'])
# print(f"студенты старше 30 состовляет: {round(lst1/len(students) * 100 ,2)}%")
# 5)
# names1 = set()
# sort = []
# for i in students:
#     h = i['name']
#     names1.add(h)
# n1 = sorted(names1)
# # print (n1)
# for x1 in n1:
#     for x in students:
#         if x1 in x['name']:
#             sort.append(x)
# for q in sort:
#     print(q)
# print ("1111111111111111111111111111111111111111111111111111111111111111111111")
# ages = set()
# sort2 = []
# for i in students:
#     h = i['age']
#     ages.add(h)
# n1 = sorted(ages)
# for x1 in n1:
#     for x in students:
#         if str(x1) in str(x['age']):
#             sort2.append(x)
# for w in sort2:
#     print(w)
# print ("1111111111111111111111111111111111111111111111111111111111111111111111")
# genders = set()
# sort2 = []
# for i in students:
#     h = i['gender']
#     genders.add(h)
# n1 = sorted(genders)
# for x1 in n1:
#     for x in students:
#         if str(x1) in str(x['gender']):
#             sort2.append(x)
# for e in sort2:
#     print(e)
# print ("1111111111111111111111111111111111111111111111111111111111111111111111")
# kurse = set()
# sort2 = []
# for i in students:
#     h = i['course']
#     kurse.add(h)
# n1 = sorted(kurse)
# for x1 in n1:
#     for x in students:
#         if str(x1) in str(x['course']):
#             sort2.append(x)
# for r in sort2:
#     print(r)
# # 6)
# for i in students:
#     if i['course'] == 'javascript':
#         i['course'] = 'python'
#     else:
#         continue
# print(students)
# # 7)
# i = 0 
# diction = {}
# while i < 3:
#     name = input("name: ")
#     age = input("age: ")
#     course = input("course: ")
#     gender = input("gender: ")
#     i += 1
#     diction = {'name': name, 'age': age, 'course': course, 'gender': gender}
#     students.append(diction)
# print(*students, sep="\n")
# # 8)
# n = []
# for i in students:
#     if i['age'] < 18:
#         n.append(i)
# for x in n:
#     if x in students:
#         students.remove(x)
# for t in students:
#     print(t)
