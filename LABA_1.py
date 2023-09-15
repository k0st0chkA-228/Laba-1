# Натуральные числа. Выводит на экран четные числа, меняя в них местами каждые две соседние цифры
# пока не встретит число из К подряд идущих нулей. После чего вывод идет без смены и прописью.


nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
ignor = ['\n', '\t', ' ']

k = int(input('введите число K = '))               # ввод K
while k < 1 :
    k = int(input('введите пожалуйста число больше 0\n'))
ex = '0' * k

buffer = []                    # рабочий буфер
zero_flag = False              # флаг числа c подряд идущими нулями

num_to_string = ['ноль', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']

with open('111111.txt', 'rt') as a:               # открытие файла
    while True:                                   # начало работы цикла
        inp = a.read(1)                           # считывание 1 символа
        if not inp:
            break
        if inp not in nums and inp not in ignor:  # если не число
            buffer = []                           # очистка рабочего буфера
            while inp not in ignor:               # пропуск мусора
                inp = a.read(1)
        if inp in ignor:                          # если число найдено
            s = ''.join(buffer)                   # преобразование буфера в строку
            if ex == s:                           # проверка на число из К нулей
                zero_flag = True
            if zero_flag and buffer:              # число остановки программы
                print(*map(lambda x: num_to_string[int(x)],  buffer))      # вывод числа прописью
            elif buffer and int(buffer[-1]) % 2 == 0:                      # проверка на четность
                for i in range(1, len(buffer), 2):
                    buffer[i], buffer[i - 1], = buffer[i - 1], buffer[i]   # перестановка соседних цифр
                s = ''.join(buffer)
                print(s)                           # вывод числа
            buffer = []                           # отчистка буфера
        else:
            buffer.append(inp)                    # заполнение рабочего буфера

