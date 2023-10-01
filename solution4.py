#Question:-Python Program for Fibonacci numbers using Recursion.

def Fibonacci(n):

	# Check if input is 0 then it will
	# print incorrect input
	if n < 0:
		print("Incorrect input")

	elif n == 0:
		return 0

	elif n == 1 or n == 2:
		return 1

	else:
		return Fibonacci(n-1) + Fibonacci(n-2)


print(Fibonacci(9))
