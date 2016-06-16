def selection_sort(list):
    for i in range(len(list)):        
        for j in range(i + 1, len(list)):
            if list[j] < list[i]:
                temp = list[i]
                list[i] = list[j]
                list[j] = temp
            
    return list
    
print(selection_sort([1, 5, 7, 2, 3, 6, 4])) # expects [1, 2, 3, 4, 5, 6, 7]
print(selection_sort([37, 56, 455, 388, 2, 6, 8])) # expects [2, 6, 8, 37, 56, 388, 455]
print(selection_sort([])) # expects []
print(selection_sort([3])) # expects [3]
print(selection_sort([6,5])) # expects [5,6]