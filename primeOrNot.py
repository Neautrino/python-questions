# Question:
# Write a Python function to check if a given number is a prime number or not. A prime number is a natural number greater than 1 that is not a product of two smaller natural numbers.
def is_prime(number):
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    
    for i in range(3, int(number**0.5) + 1, 2):
        if number % i == 0:
            return False
    return True

# Example usage
num = int(input("Enter a number: "))
if is_prime(num):
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")
