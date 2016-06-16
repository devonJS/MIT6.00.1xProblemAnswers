def left_lesser(num1, num2):
    if num1 < num2:
        return True
    else:
        return False

def merge_lists(left, right, left_lesser):
    merged_list = []
    i = 0
    j = 0
    
    while i < len(left) and j < len(right):
        if left_lesser(left[i], right[j]):
            merged_list.append(left[i])
            i += 1
        elif not left_lesser(left[i], right[j]):
            merged_list.append(right[j])
            j += 1
    
    if j == len(right):
        while i < len(left):
            merged_list.append(left[i])
            i += 1
    elif i == len(left):
        while j < len(right):
            merged_list.append(right[j])
            j += 1
    
    return merged_list
    
    
def merge_sort(list, left_lesser):
    if len(list) <= 1:
        return list[:]
    else: 
        mid = int(len(list) / 2)
        left = merge_sort(list[:mid], left_lesser)
        right = merge_sort(list[mid:], left_lesser)
        return merge_lists(left, right, left_lesser)
        
print(merge_sort([1, 5, 7, 2, 3, 6, 4], left_lesser)) # expects [1, 2, 3, 4, 5, 6, 7]
print(merge_sort([37, 56, 455, 388, 2, 6, 8], left_lesser)) # expects [2, 6, 8, 37, 56, 388, 455]
print(merge_sort([], left_lesser)) # expects []
print(merge_sort([3], left_lesser)) # expects [3]
print(merge_sort([6,5], left_lesser)) # expects [5,6]