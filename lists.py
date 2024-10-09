import time
import random

def square_number(numbers):
    start_time = time.time()
    squares = []
    for number in numbers:
        squares.append(number ** 2)
    end_time = time.time()
    view_time = end_time - start_time
    print(f"The result of squaring numbers array: {squares} ~~ The time complexity of this function is {view_time:.7f} seconds.")

def reverse_sublist(numbers, start, end):
    reverse = []
    start_time = time.time()
    reverse.append(numbers[start:end][::-1])
    end_time = time.time()
    diff_time = end_time - start_time
    print(f"The result of reversing sublist: {reverse} ~~ The time complexity of this function is {diff_time:.7f} seconds.")

def sort_list(list1, list2):
    start_time = time.time()
    list1 = sorted(list1)
    list2 = sorted(list2)
    res = sorted(list1 + list2)
    end_time = time.time()
    sorted_time = end_time - start_time
    print(f"The result of combining 2 sorted lists: {res} ~~ The time complexity of this function is {sorted_time:.7f} seconds.")





num = 50
start = 1
end = 100
numbers = []

for i in range(num):
    numbers.append(random.randint(start, end))

# square_number(numbers)

numbers.sort()

start = 0
end = 20

# print(numbers)

# reverse_sublist(numbers, start, end)

list1 = [1, 4, 7, 9, 20 , 31]
list2 = [2, 6, 8, 14, 3, 43, 8]

sort_list(list1, list2)