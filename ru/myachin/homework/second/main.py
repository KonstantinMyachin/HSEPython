# ### Задача 1
# С клавиатуры вводится строка, содержащая имена, разделённые пробелами. Для каждого имени вывести строчку 
# 
#     Hello, <имя>
#     
# Всего должно быть выведено столько строк, сколько имён написано в строке.
#     
# **Пример**
# 
# *Входные данные*
# 
#     Alice Bob Daniel
# 
# *Выходные данные*
# 
#     Hello, Alice
#     Hello, Bob
#     Hello, Daniel
#     
# **Подсказка.** Вам пригодится метод `.split()`.


def hello_names():
    names = input().split()
    for name in names:
        print("Hello, " + name)


hello_names()


# ### Задача 2
# Даны два целых числа A и B (при этом A≤B). Каждое число вводится с клавитуры, после ввода пользователь нажимает
#  «Enter». Выведите все целые числа от A до B включительно в столбик.
# 
# Здесь имеет смысл использовать цикл `for` (хотя в принципе можно обойтись и без него).
# 
# **Пример**
# 
# **Входные данные**
# 
#     3
#     6
# 
# **Выходные данные**
# 
#     3
#     4
#     5
#     6


def my_range():
    # YOUR CODE HERE
    a = int(input())
    b = int(input())
    while a <= b:
        print(a)
        a = a + 1


my_range()


# ### Задача 3
# Напишите программу, которая запрашивает целое число `n` с клавиатуры, затем `n` целых чисел, после чего выводит
# произведение всех этих чисел.
# 
# **Пример.**
# 
# **Входные данные:**
# 
#     3
#     9
#     2
#     5
# 
# **Выходные данные:**
# 
#     90


def prod_n():
    # YOUR CODE HERE
    n = int(input())
    result = 1
    for number in range(n):
        result *= int(input())
    print(result)


prod_n()


# ### Задача 4
# Факториалом натурального числа $n$ называется произведение всех натуральных чисел от 1 до $n$ включительно.
# Факториал $n$ обозначается $n!$. Например,
# $$
# 4! = 1 \times 2 \times 3 \times 4 = 24.
# $$
# Написать программу, запрашивающую натуральное число $n$ с клавиатуры, вычисляющую и печатающую $n!$.
# Использовать какие-либо библиотечные функции нельзя (то есть запрещена конструкция `import`).
# 
# **Пример.**
# 
# **Входные данные:**
# 
#     5
# 
# **Выходные данные:**
# 
#     120

def my_fact():
    # YOUR CODE HERE
    n = int(input())
    result = 1
    for number in range(1, n + 1):
        result *= number
    print(result)


my_fact()


# Числа Фибоначчии — это последовательность чисел, заданная следующим образом:
# 
# $$a_1 = 1,\quad a_2 = 1, \quad a_{k+1}=a_k+a_{k-1}$$
# 
# Ввести число `k` с клавиатуры и вывести $a_k$. Считать, что число `k` всегда больше одного. (То есть на вход никогда
# не будет подано число, меньшее или равное одного.)
# 
# 
# **Пример.**
# 
# 
# _Входные данные:_
# 
#     3
# 
# _Выходные данные:_
# 
#     2
# 
# _Входные данные:_
# 
#     5
# 
# _Выходные данные:_
# 
#     5
# 
# _Входные данные:_
# 
#     6
# 
# _Выходные данные:_
# 
#     8

def fib_k():
    # YOUR CODE HERE
    k = int(input())
    previous = 1
    pre_previous = 0
    result = 0
    for number in range(k - 1):
        result = pre_previous + previous
        pre_previous = previous
        previous = result
    print(result)


fib_k()


# ### Задача 6 (3 балла)
# 
# *Необязательная задача*
# 
# Введите число `n` с клавиатуры. Выведите таблицу умножения от 1 до `n` включительно, как показано в примере.
# Допустимо, чтобы каждая строка заканчивалась пробелом.
# 
# **Пример**
# 
# _Входные данные_
# 
#     5
# 
# _Выходные данные_
# 
#     1 2 3 4 5 
#     2 4 6 8 10 
#     3 6 9 12 15 
#     4 8 12 16 20 
#     5 10 15 20 25 
#     
# **Подсказка.** Вам понадобятся вложенные циклы — цикл внутри цикла. Также может оказаться полезным следующее знание: `print` по умолчанию добавляет в конец строки символ перевода строки (то есть каждый следующий `print` печатает с новой строки). Чтобы он этого не делал, можно добавить ему именованный аргумент `end`. Например, попробуйте запустить следующий код:
# 
#     print("Hello", end="!!!")
#     print("World")

def mult_table():
    # YOUR CODE HERE
    n = int(input())
    for i in range(n):
        for j in range(n):
            print((i + 1) * (j + 1), end=" ")
        print()


mult_table()


# ### Задача 7 (4 балла)
# 
# *Необязательная задача*
# 
# Не пользуясь библиотечными функциями, для вводимого с клавиатуры натурального $n$, вывести на экран первые $n$
# строк [треугольника Паскаля](https://ru.wikipedia.org/wiki/%D0%A2%D1%80%D0%B5%D1%83%D0%B3%D0%BE%D0%BB%D1%8C%D0%BD%D0%B8%D0%BA_%D0%9F%D0%B0%D1%81%D0%BA%D0%B0%D0%BB%D1%8F). Элементы должны быть разделены пробелами. Допустимо наличие пробела в конце строки.
# 
# **Пример**
# 
# **Входные данные**
# 
#     5
# 
# **Выходные данные**
# 
#     1
#     1 1
#     1 2 1
#     1 3 3 1
#     1 4 6 4 1


def pascal_triangle():
    n = int(input())
    prev = [1]
    print(*prev)
    for i in range(n - 1):
        new = [1]
        for k in range(len(prev) - 1):
            new.append(prev[k] + prev[k + 1])
        new.append(1)
        for k in new:
            print(k, end=" ")
        print()
        prev = new


pascal_triangle()


# ### Задача 8
# Написать программу, которая запрашивает целое число `n` с клавиатуры, а затем `n` строк.
# (Каждая строка запрашивается отдельно, то есть после очередного запроса пользователь дожен нажать `Enter`.)
# После этого она должна вывести список, в который записаны эти строки, в том порядке, в котором они записаны.
# 
# **Пример**
# 
# _Входные данные_
# 
#     3
#     This
#     is
#     a test
# 
# _Выходные данные_
# 
#     ['This', 'is', 'a test']
# 
# **Подсказка** Введите сначала число `n` таким образом, как это обычно делалось. Затем создайте пустой список `[]`
# и присвойте его какой-нибудь переменной. После этого создайте цикл, который должен исполниться ровно `n` раз
# (для этого необходимо использовать функцию `range()`), в теле цикла вводите очередную строку и записывайте её в
# список с помощью `.append()`.


def input_strings():
    # YOUR CODE HERE
    n = int(input())
    strings = []
    for number in range(n):
        strings.append(input())
    print(strings)


input_strings()


# ### Задача 9
# Написать программу, которая запрашивает целое число `n` с клавиатуры, а затем `n` строк.
# (Каждая строка запрашивается отдельно, то есть после очередного запроса пользователь дожен нажать `Enter`.)
#  После этого она должна вывести эти строки в обратном порядке — последнее становится первым и т.д.
#
# **Пример**
#
# _Входные данные_
#
#     3
#     This
#     is
#     a test
# 
# _Выходные данные_
# 
#     a test
#     is
#     This
# 
# **Подсказка** Вы можете использовать метод `.reverse()` для списков или срез `[::-1]`.


def last_in_first_out():
    # YOUR CODE HERE
    n = int(input())
    strings = []
    for number in range(n):
        strings.append(input())
    strings.reverse()
    for s in strings:
        print(s)


last_in_first_out()


# ### Задача 10 (2 балла)
# С клавиатуры вводится строка, состоящая из нескольких предложений. Каждое предложение заканчивается точкой.
# Все слова разделены пробелами. После точек тоже ставится пробел (если это не самая последняя точка).
# Никаких других знаков препинания нет. Для каждого предложения вывести его первое и последнее слово.
# 
# **Пример**
# 
# _Входные данные_
# 
#     One two three. Hello World. This is just a test.
# 
# _Выходные данные_
# 
#     One three
#     Hello World
#     This test
# 
# **Подсказка.** Если передать методу `.split()` параметр, то он будет использовать его в качестве разделителя.
# Например, попробуйте посмотреть, что выдаст `"Hello, World! This is a test! Okay?".split("!")`.
# Чтобы избавиться от пробелов в начале и конце строки можно использовать метод `.strip()`.


def first_last_word():
    # YOUR CODE HERE
    s = input().strip()
    sentences = s.split(".")
    for sentence in sentences:
        words = sentence.split()
        if (len(words) > 1):
            print(words[0], end=" ")
            print(words[(len(words) - 1)])


first_last_word()


# ### Задача 11 (3 балла)
# С клавиатуры вводится целое число, разбивается на цифры и каждая цифра записывается словом.
# Результат выводится с большой буквы, разделенный пробелами.
# 
# Запрещено использовать оператор `if`.
# 
# **Пример.**
# 
# _Входные данные_
# 
#     123
# 
# _Выходные данные_
# 
#     One two three
# 
# _Входные данные_
# 
#     5023
# 
# _Выходные данные_
# 
#     Five zero two three
# 
# В выходной строке в конце может быть лишний пробел.
# 
# **Подсказка** В цикле `for` строка будет вести как список, состоящий из отдельных символов.
# Чтобы сделать первую букву строки большой, используйте метод `.capitalize()`.


def digits_to_stings():
    # YOUR CODE HERE
    numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    s = input()
    result = ""
    for c in s:
        result += numbers[int(c)]
        result += " "
    print(result.capitalize())


digits_to_stings()
