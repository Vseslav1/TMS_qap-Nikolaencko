# # print('hello world')
# #
# # print('hello world')
#
# name = "vseslav"
# surname = "nikoaenko"
# age = 26
#
# print(name,surname,age)
#
# name = 'JohnSnow'
# age = 29
#
# print(name,age)
import getpass


# # ДЗ 3
# # 1 Привести к целому типу - 1.6, 2.99
#
a = int(1.6)
b = int(2.99)

print(a,b)

# # 2 Заменить символ “#” на символ “/” в строке 'www.my_site.com#about'
#
text = "www.my_site.com#about"

c = text.replace('#','/')

print(c)

# 3 Напишите программу, которая добавляет ‘ing’ к слову ‘stroka’
#
text = ['stroka','ing']

resultat = ''.join(text)

print(resultat)



# 4 В строке “Ivanou Ivan” поменяйте местами слова => "Ivan Ivanou"

a = 'Ivanou Ivan'

b = a.split()

c = ['Ivanov','Ivan']

c.reverse()

b = ' '.join(c)

print(b)





# 5 Напишите программу которая удаляет пробел в начале, в конце строки

text = " Напишите программу которая удаляет пробел в начале, в конце строки "
text = text.strip()

print(text)

# 6 Создайте словарь, связав его с переменной school, и наполните его данными которые бы отражали количество учащихся
# в десяти разных классах (например, 1а, 1б, 2б, 6а, 7в и т.д.).

dict = 'school'


school =[
    {'class': '1A','number of students': '23'},
    {'class': '2A','number of students': '33'},
    {'class': '3A','number of students': '21'},
    {'class': '4A','number of students': '19'},
    {'class': '5A','number of students': '11'},
    {'class': '1b','number of students': '22'},
    {'class': '1c','number of students': '24'},
    {'class': '4c','number of students': '18'},
    {'class': '11a','number of students': '25'},
    {'class': '9b','number of students': '14'},
    {'class': '10b','number of students': '17'}
]

print(school[10].keys())

# 7 Создайте список и извлеките из него списка второй элемент.

list_mix =[1,'2',3,4,5,6,False]
#
#
print(list_mix[1])

# 8 Вывести входит ли строка1 в строку2 (пример: employ и employment )

str1 = 'стол'
strochka2 = 'столешница'
if strochka2.find('стол') == 0:
    print('yes')

# 9 Вывести нужные символы
x = "My name is Agent Smith"

 print(x[1]) #y

print(x[3],x[6],x[9],x[12],x[15])  #nesgt

# 10 Есть массив чисел. Известно, что каждое число в этом массиве имеет пару, кроме одного: [1, 5, 2, 9, 2, 9, 1] => 5
# Напишите программу, котораяпппппп будет выводить уникальное число


list1 = [1, 5, 2, 9, 2, 9, 1]
a = []
for i in list1:
    if list1.count(i) == 1: #количество вхождений
        a.append(i)
print(a)



# задание с ур

text1 = "HEllO WORLD"
text2 = " "
text3= "!"

sum = text1 + text2 + text3

print(sum)


