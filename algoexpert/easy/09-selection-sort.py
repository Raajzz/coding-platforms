def selectionSort( array ):
  for i in range( len(array)-1 ):
    min_pos = i 
    for j in range( i + 1, len(array) ):
      if( array[j] < array[min_pos] ):
        min_pos = j 
    array[min_pos], array[i] = array[i], array[min_pos]
  return array

print(selectionSort([8, 5, 2, 9, 5, 6, 3]))