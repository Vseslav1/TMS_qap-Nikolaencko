# Работа с переменными:
# 1 Переменной var_int присвойте значение 10, var_float - значение 8.4, var_str - "No".

var_int = 10
var_float = 8.4
var_str = 'No'

# 2 Измените значение, хранимое в переменной var_int, увеличив его в 3.5 раза,
# результат свяжите с переменной big_int.

big_int = var_int * 3.5

# 3 Измените значение, хранимое в переменной var_float, уменьшив его на единицу,
# результат свяжите с той же переменной.

var_float = var_float - 1

# 4 Разделите var_int на var_float, а затем big_int на var_float. Результат данных
# выражений не привязывайте ни к каким переменным.

result1 = var_int/var_float
result2 = big_int/var_float

# 5 Измените значение переменной var_str на "NoNoYesYesYes". При формировании
# нового значения используйте операции конкатенации (+) и повторения строки (*).

var_str = var_str * 2 + 'Yes' * 3


# 6 Выведите значения всех переменных.

print(var_int, big_int, var_float, result1, result2, var_str, sep='\n')


# Строки:
# 1 Свяжите переменную с любой строкой, состоящей не менее чем из 8 символов.
# Извлеките из строки первый символ, затем последний, третий с начала и третий с
# конца. Измерьте длину вашей строки.

a = 'hello world'

b = a[0]
c = a[-1]
d = a[2]
f = a[-3]
e = len(a)
print(a, b, c, d, f, e, sep='\n')

# 2 Присвойте произвольную строку длиной 10-15 символов переменной и извлеките из
# нее следующие срезы:

str2 = 'Happy new year'

# первые восемь символов

str3 = str2[0:8]

# четыре символа из центра строки

str4 = len(str2) // 2
str4 = str2[str4 - 2: str4 + 2]

# символы с индексами кратными трем

str5 = str2[::3]

# переверните строку

str6 = str2[::-1]

# Есть строка: “my name is name”. Напечатайте ее, но вместо 2ого “name” вставьте
# 3

str7 = 'my name is name'
namemy = 'vseslav'
str8 = str7.replace('name', namemy,2 )
str9 = str8.replace('vseslav','name',1 )
print(str9)

# 4 Есть строка: test_tring = "Hello world!", необходимо

test_tring = "Hello world!"

# напечатать на каком месте находится буква w

plase = test_tring.find('w')

# кол-во букв l

kol = test_tring.count('l')
print(kol)

# Проверить начинается ли строка с подстроки: “Hello”

start = test_tring.startswith('hello')

# Проверить заканчивается ли строка подстрокой: “qwe”

end = test_tring.endswith('qwe')

# Списки:
# 1 Создайте два любых списка и свяжите их с переменными.

list1 = [1, 2, 3, 4, 5]
list2 = [11, 12, 13, 14, 15]

# 2 Извлеките из первого списка второй элемент.

b1 = list1[1]

# 3 Измените во втором списке последний элемент. Выведите список на экран.

list2[-1] = 22
print(list2)

# 4 Соедините оба списка в один, присвоив результат новой переменной. Выведите
# получившийся список на экран.

list3 = list1 + list2
print(list3)

# 5 "Снимите" срез из соединенного списка так, чтобы туда попали некоторые части
# обоих первых списков. Срез свяжите с очередной новой переменной. Выведите
# значение этой переменной.

list4 = list3[4:7]
print(list4)

# 6 Добавьте в список два новых элемента и снова выведите его.

list4.insert(0, 33)
list4.append(22)
print(list4)

# 7 Даны списки:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89];
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13].



# Нужно вернуть список, который состоит из элементов, общих для этих двух
# списков. -- !не использовать циклы

a2 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

d3 = list(set(a2) & set(b2))
print(d3)

# 8 Есть список: [1, 2, 3, 4, 3, 2, 5, 1, 4, 6, 7, 1, 8, 2, 3] оставить в нем только уникальные
# значения. !не использовать циклы

spisok1 = [1, 2, 3, 4, 3, 2, 5, 1, 4, 6, 7, 1, 8, 2, 3]
spisokunik = list(set(spisok1))
print(spisokunik)


# Логические операции:
# 1 Присвойте двум переменным любые числовые значения.

a = 32
b = 33

# 2 Составьте четыре сложных логических выражения с помощью оператора and, два из
# которых должны давать истину, а два других - ложь.

pr1 = (a < 3) and (b < 4)
pr2 = (a / 2 == 16) and (b - 1 == 32)
pr3 = (a > 3) and (b > 4)
pr4 = (a * 2 < 1) and (b * 2 < 1)
print(pr1, pr2, pr3, pr4)

# 3 Аналогично выполните п. 2, но уже используя оператор or.

pr5 = (a < 3) or (b < 4)
pr6 = (a / 32 == 1) or (b / 33 == 1)
pr7 = (a > 3) or (b > 4)
pr8 = (a * 2 < 1) or (b * 2 < 1)
print(pr5, pr6, pr7, pr8)

# 4 Попробуйте использовать в сложных логических выражениях работу с переменными
# строкового типа.

pr9 = 'coca'
pr10 = 'cola'

pr11 = (len(pr9) == 4) and (pr10 == 'cola')
pr12 = (len(pr9) == 5) or (pr10 == 'colc')
print(pr11, pr12)



# Словари:
# 1 Создайте словарь, связав его с переменной school, и наполните его данными,
# которые бы отражали количество учащихся в десяти разных классах (например, 1а, 1б,
# 2б, 6а, 7в и т.д.).

school = {
    '1a': 23,
    '2b': 24,
    '3c': 34,
    '4a': 25,
    '2f': 26,
    '1d': 27,
    '3a': 28,
    '1c': 29,
    '2d': 23,
    '2r': 24,
    '3n': 34,
    '4m': 25,
}

# 2 Узнайте сколько человек в каком-нибудь классе.

kol = school['1a']

# 3 Представьте, что в школе произошли изменения, внесите их в словарь:
# ◦ в трех классах изменилось количество учащихся;

# ◦ в школе появилось два новых класса;

school['1e'] = 35
school['11b'] = 22

# ◦ в школе расформировали один из классов.

del school['2r']

# 4 Выведите содержимое словаря на экран.

print(school)

# Преобразование типов
# 1
# Перевести строку в массив
# "Robin Singh" => ["Robin”, “Singh"]
# "I love arrays they are my favorite" => ["I", "love", "arrays", "they", "are", "my", "favorite"]

str9 = 'Robin Singh'
str10 = 'I love arrays they are my favorite'

list5 = str9.split()
lits6 = str10.split()
print(list5, lits6)

# 2
# Дан список: [‘Ivan’, ‘Ivanou’], и 2 строки: Minsk, Belarus

list7 = ['Ivan', 'Ivanov']
str12 = 'Minsk'
str13 = 'Belarus'
str_sp = ' '.join(list7)
# Напечатайте текст: “Привет, Ivan Ivanou! Добро пожаловать в Minsk Belarus”

text = f'Привет {str_sp} ! Добро пожаловать {str12} {str13}'
print(text)

# 3
# Дан список ["I", "love", "arrays", "they", "are", "my", "favorite"] сделайте из него
# строку => "I love arrays they are my favorite"

list9 = ["I", "love", "arrays", "they", "are", "my", "favorite"]
d = ' '.join(list9)
print(d)
# 4
# Создайте список из 10 элементов, вставьте на 3-ю позицию новое значение,
# удалите элемент из списка под индексом 6

list_el = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
list_el[3] = 12
del list_el[6]
print(list_el)

# 5
# Есть 2 словаря

a_sl = {'a': 1, 'b': 2, 'c': 3}
b_sl = {'c': 3, 'd': 4, 'e': 5}

# Необходимо их объединить по ключам, а значения ключей поместить в список, если у
# одного словаря есть ключ "а", а у другого нету, то поставить значение None на
# соответствующую позицию(1-я позиция для 1-ого словаря, вторая для 2-ого)
# ab = {'a': [1, None], 'b': [2, None], 'c': [3, 3], 'd': [None, 4], 'e': [None, 5]}

sl_keys = set(a_sl.keys()).union(set(b_sl.keys()))
c_sl = {
    key: [a_sl.get(key, None), b_sl.get(key, None)]
    for key in sl_keys
}
print(c_sl)

# Условия
# 1
# Дано целое число. Если оно является положительным, то прибавить к нему 1; в
# противном случае не изменять его. Вывести полученное число.

a_n = -1

r1 = (a_n + 1) if a_n > 0 else a_n

print(r1)
# 2
# Даны три целых числа. Найти количество положительных чисел в исходном
# наборе.

a_s = 3
a_f = 4
a_q = 5
sum=0
if a_s >0:
    sum +=a_s
if a_f >0:
    sum +=a_f
if a_q >0:
    sum +=a_q
print(sum)


# 3
# Дан номер года (положительное целое число). Определить количество дней в
# этом году, учитывая, что обычный год насчитывает 365 дней, а високосный — 366
# дней. Високосным считается год, делящийся на 4, за исключением тех годов, которые
# делятся на 100 и не делятся на 400 (например, годы 300, 1300 и 1900 не являются
# високосными, а 1200 и 2000 являются).

year = 1300

if year % 4 == 0:
    if year % 100 == 0 and year % 400 != 0:
        print(365)
    else:
        print(366)
else:
    print(365)

# 4
# Дано целое число в диапазоне 1–7. Вывести строку — название дня недели,
# соответствующее данному числу (1 — «понедельник», 2 — «втор- ник» и т. д.).

a = 1
dn = {
    1: 'ponedelnik',
    2: 'vtornik',
    3: 'sreda',
    4: 'chetverg',
    5: 'pyatnicza',
    6: 'sybbota',
    7: 'voskresen'
}

if a == 1:
    print(dn[1])


# 5
# Единицы массы пронумерованы следующим образом: 1 — килограмм, 2 —
# миллиграмм, 3 — грамм, 4 — тонна, 5 — центнер. Дан номер единицы массы (целое
# число в диапазоне 1–5) и масса тела в этих единицах (вещественное число). Найти
# массу тела в килограммах.

mas_i = 2
mas_f = 12000000

if mas_i == 1:
    print(mas_f)
elif mas_i == 2:
    print(mas_f / 1000000)
elif mas_i == 3:
    print(mas_f / 1000)
elif mas_i == 4:
    print(mas_f * 1000)
elif mas_i == 5:
    print(mas_f * 100)

# Цикл for
# 1
# Даны два целых числа A и B (A < B). Найти сумму всех целых чисел от A до B
# включительно.
a = 22
B = 33

c = 0

for i in range(a, b + 1):
    c += i
    print(c)

# 2
# Найти сумму всех натуральных чисел в от A до B
c2 = 0
for i in range(max(1, a), b):
    c2 += i
print(c2)

# 3
# Найти произведение положительных, сумму и количество отрицательных
# из 10 введенных целых значений.

zn = [1, 2, 3, 4, 5, -1, -4, -6, 10, -11, 7,]

summ = 0
cont = 0
pol = 1

for i in zn:
    if zn[i] > 1:
        pol *= zn[i]
    if zn[i] < 0:
        summ += zn[i]
    if zn[i] < 0:
        cont += 1


print(f'произведение положительных значений - {pol}, сумма отрицательных значений - {summ},'
      f'количество отрицательных значений - {cont}')




# 4
# Дан словарь пловцов с их результатами. Напечатать лучший результат
# заплыва среди 6 участников.
# Бекиш Александр - 21,07
# Будник Алексей - 20,34
# Гребень Анастасия - 22,12
# Давидович Татьяна - 30
# Дешук Дмитрий - 24.01
# Казак Анна - 28,17

maximym = 0
list_sw = {
    'Бекиш Александр': 21.07,
    'Будник Алексей': 20.34,
    'Гребень Анастасия': 22.12,
    'Давидович Татьяна': 30,
    'Дешук Дмитрий': 24.01,
    'Казак Анна': 28.17
}

for i in list_sw:
    if list_sw[i] > maximym:
        maximym = list_sw[i]
print(maximym)

# Есть массив чисел. Известно, что каждое число в этом массиве имеет пару,
# кроме одного: [1, 5, 2, 9, 2, 9, 1] => 5 Напишите программу, которая будет выводить
# уникальное число

list1 = [1, 5, 2, 9, 2, 9, 1]
a = []
for i in list1:
    if list1.count(i) == 1:
        a.append(i)
print(a)

# Цикл while
# 1
# Дано число N. Найти произведение всех чисел от 0 до N.

n = 6
i = 1
t = 1

while i <= n:
    t *= i
    i += 1
    print(t)


# 2
# Поле засеяли цветами двух сортов на площади S1 и S2. Каждый год
# площадь цветов первого сорта увеличивается вдвое, а площадь второго сорта
# увеличивается втрое. Через сколько лет площадь первых сортов будет
# составлять меньше 10% от площади вторых сортов.

S1 = 8
S2 = 10
years = 0

while S1 >= 0.1 * S2:
    S1 *= 2
    S2 *= 3
    years += 1
print(years)

# Дано целое число N (>0). Используя операции деления нацело и взятия
# остатка от деления, найти количество и сумму его цифр.

n = 4312
count = 0
summ = 0
while n > 0:
    last_elem = n % 10
    summ = summ + last_elem
    n = n // 10
    count += 1
print(count, summ)

n = str(n)
for i in n:
    i = int(i)
    summ += 1
    count += 1
print(count, summ)

# 4
# Деду M лет, а внуку N лет. Через сколько лет дед станет вдвое старше
# внука. И сколько при этом лет будет деду и внуку.

D = 69
V = 12
year = 0

while V * 2 != D:
    D += 1
    V += 1
    year += 1
print(D, V, year)