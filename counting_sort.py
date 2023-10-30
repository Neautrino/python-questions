#Stable Counting Sort is an efficient, non-comparison sorting algorithm that sorts a list of integers while preserving the relative order of equal elements. It is considered a "stable" sorting algorithm, which means that it maintains the original order of equal elements in the sorted output. 

#The following is a counting sort algorithm however this is a stable version of the original algorithm. 
#stable here means that the relative order of elements (in relation to the original list) is maintained such that if there are two elements that are equal, one will appear before the other in the sorted list as well

def counting_sort_stable(new_list):
    """
    Sorts a list of integers in ascending order while preserving the relative order of equal elements.
    """
    #finding maximum 
    max_item = new_list[0]
    for i in new_list:
        if max_item < i:
            max_item = i
    #make frequency array size of max item
    freq_array = [None]*(max_item+1)
    for i in range(len(freq_array)):
        freq_array[i]=[]
    #update frequency array 
    for i in new_list:
        freq_array[i].append(i)
    sorted_list = []
    for i in range(len(freq_array)):
        if len(freq_array[i]) != 0:
            for j in freq_array[i]:
                sorted_list.append(j)
    #sorted list 
    return sorted_list