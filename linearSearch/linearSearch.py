def linear_search(arr, target):
    """
    Perform a linear search to find the target element in the given array.
    
    :param arr: The list or array to search.
    :param target: The element to find.
    :return: The index of the target element if found, or -1 if not found.
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Target found, return its index
    return -1  # Target not found in the array

# Example usage:
my_list = [3, 6, 8, 12, 15, 17, 20]
target_element = 12
result = linear_search(my_list, target_element)

if result != -1:
    print(f"Element {target_element} found at index {result}.")
else:
    print(f"Element {target_element} not found in the list.")
