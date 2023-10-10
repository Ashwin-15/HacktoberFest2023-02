# Python program to check implement cycle sort
def cyclicSort(arr, n):
	i = 0
	while i < n:
		# as array is of 1 based indexing so the
		# correct position or index number of each
		# element is element-1 i.e. 1 will be at 0th
		# index similarly 2 correct index will 1 so
		# on...
		correct = arr[i] - 1
		if arr[i] != arr[correct]:
		
			# if array element should be lesser than
			# size and array element should not be at
			# its correct position then only swap with
			# its correct position or index value
			arr[i], arr[correct] = arr[correct], arr[i]
		else:
			# if element is at its correct position
			# just increment i and check for remaining
			# array elements
			i += 1


def printArray(arr):
	print(*arr)

arr = [3, 2, 4, 5, 1]
n = len(arr)
print("Before sorting array:")
printArray(arr)

# Function Call
cyclicSort(arr, n)
print("Sorted array:")
printArray(arr)

# This Code is Contributed by Prasad Kandekar(prasad264)
