def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Taking input from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Calculating and displaying the GCD
gcd = find_gcd(num1, num2)
print(f"The GCD of {num1} and {num2} is {gcd}")