# stack methods in list
my_list = [1, 5, 10]
el = my_list.pop()
print(el)
print(my_list)
my_list = [4]
print(my_list[0:-1])

# Задача: Написать функцию column(table, i), возвращающую i'ый столбец таблцы
table = [[2, 3, 3],
         [5, 10, 15]]


def column(table, i):
    return [row[i] for row in table]


print(column(table, 1))
assert column([[1, 2, 3],
               [5, 10, 15]], 1) == [2, 10]

# Working with files
f = open("test.txt")
for line in f:
    print(line.rstrip())

f.close()

f = open("test.txt")
for line in f:
    print(line.rstrip())

f.seek(0)

print("Once more")

for line in f:
    print(line.rstrip())
f.close()

f = open("test.txt")
lines = f.readlines()
f.close()
print(lines)

f = open("test.txt")
text = f.read()
f.close()
print(text)

f = open("new.txt", "w")
print("Hello! This is new file.", file=f)
f.close()

with open("new.txt", "w") as f:
    print("Hello! This is new file.", file=f)
    print(f.closed)
print(f.closed)

with open("new.txt", "a") as f:
    print("New line here", file=f)

with open("new.txt") as nf, open("test.txt") as tf:
    print(nf.readlines())
    print(tf.readlines())

numbers = [1, 2, 5.5, 17.5] * 100
print(len(numbers))

# Создать список squares, состоящий из квадратов чисел в numbers
squares = [number ** 2 for number in numbers]
print(squares[:5])

# numpy lib
import numpy as np

arr = np.array([3, 18, 4])
print(arr[1])
arr[0] = 12
print(arr)

u = np.array([1, 2, 3])
v = np.array([5, 10, 15])
print(u + v)
print(u * v)
print(u @ v)

mixed_array = np.array([1, 5, "hello"])
print(mixed_array)
mixed_array[0] = "This is a test. This is just a test"
print(mixed_array)

print(arr + 10)
n_arr = np.concatenate([np.array([1, 2]), np.array([3, 4])])
print(n_arr)

arr_numbers = np.array(numbers)
arr_squares = arr_numbers ** 2
print(arr_squares)

arr = np.array([0, 10, 20, 30])
some_slice = arr[1:3]
print(some_slice)
some_slice[0] = 100
print(arr)
print(some_slice.base)
arr = np.array([-5, 7, -3, 3, 12, -5])
print(arr[arr > 0])
print(arr > 0)
print(arr[np.array([False, True, True, False, True, True])])
print(arr[(arr > 0) & (arr % 2 == 0)])
print((arr > 0) & (arr % 2 == 0))
print(arr[~(arr > 0)])
arr[arr < 0] = 0
print(arr)

x = np.array([1, 2, 3, 4])
y = np.array([2, -3, 5, -7])
print(x[y > 2])

m = np.array([[1, 2, 3],
              [4, 5, 10]])
print(m.shape)
print(m[0, 2])
print(m[0, 1:3])
print(m[:, 1])
print(m.mean())
print(m.mean(axis=0))
print(m.mean(axis=1))
print(m.sum(axis=0))
print(m.sum(axis=1))
print(m + 5)

w = np.array([[3, 7, 9],
              [6, 8, 9]])
print(m + w)
print(m.T)
i = np.array([[1, 0], [0, 2]])
print(i @ m)
print(np.linalg.inv(i))
print(m + np.array([1, 2, 3]))

q = np.array([1, 2, 3, 4, 5, 6])
print(q.reshape((2, 3)))
print(q.reshape((3, 2)))
print(q.reshape((3, -1)))
print(q.reshape((1, -1)))
print(q.reshape((-1, 1)))

a = np.array([[2, 3], [1, 4]])
print(np.linalg.eig(a))

import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 21)
print(x)
x = np.linspace(-5, 5, 201)
print(x)
plt.plot(x, np.sin(x))

plt.plot(x, np.sin(x), '-.', label="$y=\\sin x$")
plt.plot(x, np.cos(x ** 2), label="$y\\cos x^2$")
plt.legend(loc=3)
