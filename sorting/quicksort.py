data = [10, 5, 11, 0, 5, 7, 1, 1, 2, 4]
expects = [11, 10, 7, 5, 5, 4, 2, 1, 1, 0]
expects2 = [0, 1, 1, 2, 4, 5, 5, 7, 10, 11]

def quick_sort(unsorted_values:list=[], ordering="asc"):
    unsorted_copy = unsorted_values.copy()
    if(len(unsorted_values) <= 1): return unsorted_values
    
    pivot = unsorted_copy.pop()
    smaller_values = []
    higher_values = []

    for item in unsorted_copy: 
        if item > pivot and ordering == "asc":
            higher_values.append(item)
        elif item < pivot and ordering != "asc":
            higher_values.append(item)
        else:
            smaller_values.append(item)
            
    return quick_sort(smaller_values, ordering) + [pivot] + quick_sort(higher_values, ordering)

def buble_sort(unsorted_values:list=[], ordering="asc"):
    unsorted_copy = unsorted_values.copy()
    index = 1
    while index < len(unsorted_copy):
        current = unsorted_copy[index]
        prev = unsorted_copy[index - 1]
        if current < prev and ordering == "asc":
            unsorted_copy[index] = prev
            unsorted_copy[index - 1] = current
            index = 1
        elif current > prev and ordering != "asc":
            unsorted_copy[index] = prev
            unsorted_copy[index - 1] = current
            index = 1
        else: index += 1

    return unsorted_copy
        


quick_sort_res = quick_sort(data, "desc")
buble_sort_res = buble_sort(data, "desc")

print(quick_sort_res)
print(buble_sort_res)