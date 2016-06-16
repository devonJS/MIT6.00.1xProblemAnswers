def bubble_sort(list):
    no_switch = False
    while not no_switch:
        no_switch = True
        for i in range(len(list) - 1):
            if list[i + 1] < list[i]:
                temp = list[i]
                list[i] = list[i + 1]
                list[i + 1] = temp
                no_switch = False
    return list
        
print(bubble_sort([1, 5, 7, 2, 3, 6, 4])) # expects [1, 2, 3, 4, 5, 6, 7]
print(bubble_sort([37, 56, 455, 388, 2, 6, 8])) # expects [2, 6, 8, 37, 56, 388, 455]
print(bubble_sort([])) # expects []
print(bubble_sort([3])) # expects [3]
print(bubble_sort([6,5])) # expects [5,6]