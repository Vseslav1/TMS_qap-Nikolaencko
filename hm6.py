# 1 Дан файл целых чисел, содержащий не менее четырех элементов.
# Вывести первый, второй, предпоследний и последний элементы данного
# файла. Если чисел меньше 3 выводить ошибку

with open('celchisl.txt', 'w') as file:
    file.write('1 2 3 4 5 6')

with open('celchisl.txt', 'r') as file:
    numbers_str = file.readline().split()
    if len(numbers_str) <= 3:
        print('ERR')
    else:
        numbers = [int(num) for num in numbers_str]
        f_e = numbers[0]
        s_e = numbers[1]
        t_e = numbers[-1]
        l_e = numbers[-2]
        print(f_e, s_e, t_e, l_e)



# 2 Дан файл целых чисел. Создать два новых файла, первый из которых
# содержит четные числа из исходного файла, а второй — нечетные (в том
# же порядке). Если четные или нечетные числа в исходном файле
# отсутствуют, то соответствующий результирующий файл оставить пустым.

chet = []
nechet = []
with open('celchisl.txt', 'r') as file:
    numbers_str = file.readline().split()
    numb = [int(num) for num in numbers_str]
for num1 in numb:
    if num1 % 2 ==0:
        chet.append(num1)
    if num1 % 2 != 0:
        nechet.append(num1)
chet_st = ' '.join(str(i) for i in chet)
nechet_st = ' '.join(str(i) for i in nechet)

with open('1ch.txt', 'w') as file:
    file.write(chet_st)

with open('1nech.txt','w') as file:
    file.write(nechet_st)

# 3 Дан файл вещественных чисел. Заменить в нем все элементы на их
# квадраты.

kvdr = []
with open('vesh.txt', 'r') as file:
    numbers_str = file.readline().split()
    numb = [float(num) for num in numbers_str]
for num in numb:
    kvdr_num = num ** 2
    kvdr.append(kvdr_num)

kvdr_st = ' '.join(str(i) for i in kvdr)

with open('vesh.txt', 'w') as file:
    file.write(kvdr_st)


# 4 Даны два файла произвольного типа. Поменять местами их
# содержимое. Файлы должны быть бинарного типа


with open('file.bin', 'rb') as f1:
    data1 = f1.read()

with open('file2.bin', 'rb') as f2:
    data2 = f2.read()

with open('file.bin', 'wb') as f1:
    f1.write(data2)

with open('file2.bin', 'wb') as f2:
    f2.write(data1)