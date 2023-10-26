#program to find largest and smallest number and then display it's sum
def find_smallest_largest_and_sum(numbers):
    if not numbers:
        return None, None, None

    smallest = float('inf')
    largest = float('-inf')

    for num in numbers:
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num

    return smallest, largest, smallest + largest

# Prompting user for input
num_count = int(input("How many numbers do you want to enter? "))
numbers = []

for i in range(num_count):
    num = float(input(f"Enter number {i + 1}: "))
    numbers.append(num)

# Finding smallest, largest, and their sum
smallest, largest, total = find_smallest_largest_and_sum(numbers)

if smallest is not None and largest is not None:
    print(f"The smallest number is {smallest}")
    print(f"The largest number is {largest}")
    print(f"The sum of the smallest and largest numbers is {total}")
else:
    print("The list is empty, cannot determine smallest and largest.")
