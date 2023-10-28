def bubble_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place, so we don't need to check them
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Taking user input for the list
user_input = input("Enter elements of the list separated by space: ")
input_list = list(map(int, user_input.split()))

# Sorting the user input list using bubble_sort function
bubble_sort(input_list)

# Displaying the sorted list
print("Sorted Array:", input_list)
