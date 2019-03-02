# array and iterator
numbers = [7, 8, 12, 765, 3, 8, 65.7]
result = 0
for number in numbers:
    result += number

print(result)

# split function
some_str = "this is a test"
words = some_str.split()
print(words)

another_str = "Hello, world! This is a test!"
sentences = another_str.split("!")
print(sentences)

# join function
words = ["hello", "world", "test"]
line = ", ".join(words)
print(line)

# range function
for i in range(5):
    print("Hello!")
    print("i = ", i)

range_list = list(range(5))
print(range_list)

range_list = list(range(2, 5))
print(range_list)

range_list = list(range(2, 18, 3))
print(range_list)

# part of array
my_list = [0, 10, 20, 30, 40, 50]
print(my_list[2:4])
print(my_list[1:5:2])
print(my_list[::-1])

# creating array of integers from array of strings
numbers_as_str = ['7', '12', '3', '45']
# создать список, в котором эти числа записаны как числа
numbers_as_int = []
for number in numbers_as_str:
    numbers_as_int.append(int(number))

print(numbers_as_int)

# type of value
print(type(3.))

# unmodified list (tuple)
my_tuple = (6, 12, "12")
print(my_tuple)
print(my_tuple[1])

# error
# my_tuple[1] = 1

pairs = [(1, 6), (8, 3), (2, 5), (7, 3)]
print(pairs)
print(pairs[2])

for a, b in pairs:
    print("a = ", a)
    print("b = ", b)
    print("Next item")

# for loop with indexes (enumerate function)
some_list = ["Hello", "world", "test"]
for i, element in enumerate(some_list):
    print("word", element, "position", i)

print(list(enumerate(some_list)))

numbers = [3, 8, 9, 12]
for i, x in enumerate(numbers):
    numbers[i] = x + 1

print(numbers)
