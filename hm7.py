# 1 Создать lambda функцию, которая принимает на вход имя и выводит его в формате “Hello, {name}”


name_func = lambda name: f'Hello, {name}'


print(name_func('Vseslav'))

# 2 Создать lambda функцию, которая принимает на вход список имен и выводит их в формате “Hello, {name}” в другой список

list1 = ['Aise', 'Jonn', 'Martin']

sp_in = lambda name: [f'Hello ,{name}' for name in list1]


list2 = sp_in(list1)

print(list2)

# 1 Напишите генератор который принимает список
# numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7] и озвращает новый список только с положительными числами


numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]


def pol_ch(num):
    for i in num:
        if i > 0:
            yield i


my_gen = pol_ch(numbers)


for i in my_gen:
    print(i)

# 2 Необходимо составить список чисел которые указывают на длину слов в строке
# : sentence = " thequick brown fox jumps over the lazy dog", но только если слово не "the" с обработкой исключений



sentence = "thequick brown fox jumps over the lazy dog"
list3 = sentence.split()

lengths = []
for word in list3:
    try:
        if word != "the":
            lengths.append(len(word))
    except:
        pass

print(lengths)