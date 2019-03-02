students = ["Alice", "Bob", "Claudia"]
grades = [5, 3, 4]
for student, grade in zip(students, grades):
    print(student, grade)

print(list(zip(students, grades)))


def elementwise_sum(u, v):
    """
    :param u: list of numbers
    :param v: one more list of numbers
    :return: list w
    w[i] = u[i] + v[i] for all i
    """
    return [i + j for i, j in zip(u, v)]


assert elementwise_sum([1, 2], [3, 4]) == [4, 6]

# Dictionary
grade_book = {"Alice": 5, "Bob": 3, "Claudia": 4}
print(type(grade_book))
print(grade_book["Bob"])
grade_book["Bob"] = 4
print(grade_book["Bob"])
print("Daniel" in grade_book)
print("Alice" in grade_book)
print(grade_book.get("Alice"))
print(grade_book.get("Daniel") is None)
print(grade_book.get("Daniel", "No such student"))

# Dictionary iterator
for student in grade_book:
    print(student)

for student in grade_book:
    print(student, grade_book[student])

for student, grade in grade_book.items():
    print(student, grade)

print(grade_book.items())

result = sum(grade_book.values())
print(result)
avg = result / len(grade_book)
print(avg)

print(grade_book.keys())

grade_book = {"Alice": [3, 4], "Bob": [5], "Claudia": [2, 4, 1]}
grade_book = [{"Alice": 4, "Bob": 5},
              {"Alice": 5, "Claudia": 4}]

my_dict = {"a": 5, "b": 3}
one_more_dictionary = dict.fromkeys(["1", "2", "3"], 987)
print(one_more_dictionary)

# Key of dictionary might be only immutable objects
# sums = {[2, 3]: 5, [1, 2]: 3}
# print(sums)

sums = {(2, 3): 5, (1, 2): 3}
print(sums[(2, 3)])
squares = {2: 4, 5: 25}
print(squares[2], squares.get(0))

grade_book = {"Alice": 4, "Bob": 5, "Claudia": 4, "Elizabeth": 2}


# get List of students with grade > 2
def good_students(grade_book):
    return [student for student, grade in grade_book.items() if grade > 2]


print(good_students(grade_book))
assert good_students(grade_book) == ["Alice", "Bob", "Claudia"]

print([x ** 2 for x in range(100) if x % 4 == 0])

squares = {x: x ** 2 for x in range(5)}
print(squares)

# sorting
numbers = [5, 2, 12, 3]
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)

# sorting with no modify main array
main_array = [7, 4, 2, 8]
new_array = sorted(main_array)
print(main_array)
print(new_array)

# comparing strings
print("A" < "a")
print(ord("A"), ord("a"))

sorted_names = sorted(["Bob", "Alice", "Alla", "Bill"])
print(sorted_names)

table = [[4, 5], [6, 3], [2, 5], [6, 1]]
print(sorted(table))
print([1, 4] < [2, 0])
print([1, 4] < [1, 4, 5])


# function argument can be a function
def subs2(f):
    return f(2)


def plus_odin(x):
    return x + 1


from math import sqrt

print(subs2(plus_odin))
print(subs2(sqrt))

sorted(["hello", "this", "world", "is", "the", "best"], key=len)

table = [[4, 5],
         [6, 4],
         [2, 5],
         [6, 1]]


# sort by second column
def my_sort_key(item):
    return item[1]


print(sorted(table, key=my_sort_key))
print(sorted(table, key=lambda x: x[1]))

print((lambda x: x ** 2)(100))

from operator import itemgetter

f = itemgetter(1)
print(f([6, 8, 10]))
f = itemgetter(2)
print(f([6, 8, 10]))


def my_sort_key_2(item):
    return (item[1], item[0])


print(sorted(table, key=my_sort_key_2))
