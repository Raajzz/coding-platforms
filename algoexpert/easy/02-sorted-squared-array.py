# METHOD 1 | look, first find a position beyond which we have positive numbers. Now, you have two arrays which are both sorted (either ascending or descending). Which means you can do two pointer merge sort to create a single array, now performe your squaring function

def sortedSquaredArray(array):
	pos_position = 0
	new_array = []
	for idx in range(len(array)):
		if(array[idx] < 0):
			pos_position = idx 

	left_pos = pos_position 
	right_pos = pos_position + 1

	if (left_pos == len(array) - 1):
		for idx in range(pos_position, -1, -1):
			new_array.append(array[idx]**2)
	elif (right_pos == 0):
		for idx in range(len(array)):
			new_array.append(array[idx]**2)
	else:
		while(left_pos >= 0 and right_pos < len(array)):
			if(array[left_pos]**2 < array[right_pos]**2):
				new_array.append(array[left_pos]**2)
				left_pos -= 1
			elif(array[left_pos]**2 > array[right_pos]**2):
				new_array.append(array[right_pos]**2)
				right_pos += 1
			else:
				new_array.append(array[left_pos]**2)
				new_array.append(array[right_pos]**2)
				left_pos -= 1
				right_pos += 1
		if(left_pos == -1):
			while(right_pos < len(array)):
				new_array.append(array[right_pos]**2)
				right_pos += 1
		elif(right_pos == len(array)):
			while(left_pos >= 0):
				new_array.append(array[left_pos]**2)
				left_pos -= 1

	return new_array

print(sortedSquaredArray([-3,-2,-1,1,2,3]))