# NOT COMPLETED #

def productSum(array):
  str_array = str(array)
  dp_counter = 0
  mul_counter = 1
  sum_array = 0
  for char in str_array:
    if(char != ',' and char != ' '):
      if(char == '['):
        dp_counter += 1
        mul_counter *= mul_counter*dp_counter
      elif(char == ']'):
        mul_counter /= mul_counter/dp_counter
        dp_counter -= 1
      else:
        sum_array += mul_counter*int(char)
  print(sum_array)

productSum([1,[2,[3]]])