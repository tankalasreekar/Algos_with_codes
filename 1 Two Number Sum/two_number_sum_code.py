def two_number_sum1(array, target):
	n = len(array)
	possibilities = []
	for i in range(n-1):
		for j in range(i,n):
			if array[i] + array[j] == target:
				possibilities.append([array[i],array[j]])
	return possibilities

def two_number_sum2(array, target):
	hash_table = {}
	possibilities = []
	for i in array:
		if target - i in hash_table:
			possibilities.append([i,target - i])
		else:
			hash_table[i] = True
	return possibilities

def two_number_sum3(array, target):
	array.sort()
	possibilities = []
	left, right = 0, len(array) - 1
	while left < right:
		currentSum = array[left] + array[right]
		if currentSum < target:
			left+=1
		elif currentSum > target:
			right-=1
		elif currentSum == target:
			possibilities.append([array[left], array[right]])
			left += 1
			right -= 1
	return possibilities

sample = [2,4,-3,10,5,9,12,3]
target = 7

print(two_number_sum1(sample,target))
print(two_number_sum2(sample,target))
print(two_number_sum3(sample,target))
