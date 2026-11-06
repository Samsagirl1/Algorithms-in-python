def binary_search(array, value):
    
    min_index = 0 
    max_index = len(array) - 1

    while min_index <= max_index:
        
        middle_index = (min_index + max_index) // 2
        
        if array[middle_index] > value:
            max_index = middle_index - 1  
        elif array[middle_index] < value:
            min_index = middle_index + 1
        else:
            return middle_index

        return -1