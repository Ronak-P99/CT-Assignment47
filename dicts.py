import time


def merge_dict(dict1, dict2):
    start_time = time.time()
    merged = {i: dict1.get(i, 0) + dict2.get(i, 0) 
     for i in set(dict1).union(dict2)}
    end_time = time.time()
    merge_time = end_time - start_time
    print(f"The result of merging 2 dictionaries: {merged} ~~ The time complexity of this function is {merge_time:.7f} seconds.")

def intersect_dict(dict1, dict2):
    start_time = time.time()
    intersection = {x:dict1[x] for x in dict1 if x in dict2}
    end_time = time.time()
    int_time = end_time - start_time
    print(f"The result of intersecting 2 dictionaries: {intersection} ~~ The time complexity of this function is {int_time:.7f} seconds.")

def CountFrequency(my_list):
    freq = {}
    start_time = time.time()
    for items in my_list:
        freq[items] = my_list.count(items)
 
    for key, value in freq.items():
        print("% s : % d" % (key, value))
    end_time = time.time()
    count_time = end_time - start_time
    print(f"The time complexity of this function is {count_time:.7f} seconds.")





dict1 = {'a': 2, 'b': 8, 'c': 9}
dict2 = {'d': 15, 'e': 20, 'c': 25}
my_list = ['hi', 'hi', 'bye', 'bye', 'hi', 'bye', 'bye', 'hi']

merge_dict(dict1, dict2)
intersect_dict(dict1, dict2)
CountFrequency(my_list)