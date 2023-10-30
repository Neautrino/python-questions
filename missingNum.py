'''
Given an array arr[] of size N-1 with integers in the range of [1, N], the task is to find the missing number from the first N integers.
'''

def missingNum(arr, n):
	t= [0] * (n+1)

	for i in range(0, n):
		t[arr[i] - 1] = 1

	for i in range(0, n+1):
		if(t[i] == 0):
			num = i + 1

	print(num)

arr = [1, 2, 3, 5]
n = len(arr)
missingNum(arr, n)
