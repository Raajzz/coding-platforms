# METHOD 1 |

# the method of converting list to a string is an extremely bad idea
# please don't follow that route

# the problem with the below idea is that numbers aren't preserved
# as numbers, they'll get fragmented, -123 will get fragmented.
# therefore you need to figure out workarounds to make your
# code work, like you can have an array that includeds all the
# special characters and cohesive numbers. For that you have to go
# for list checking anyway.

# def productSum(array):
#   str_array = str(array)
#   dp_counter = 0
#   mul_counter = 1
#   sum_array = 0
#   for str_counter in range(len(str_array)):
#     if(str_array[str_counter] != ',' and str_array[str_counter] != ' ' and str_array[str_counter] != '-'):
#       if(str_array[str_counter] == '['):
#         dp_counter += 1
#         mul_counter *= dp_counter
#       elif(str_array[str_counter] == ']'):
#         mul_counter /= dp_counter
#         dp_counter -= 1
#       else:
#         print(mul_counter, str_array[str_counter])
#         sum_array += mul_counter*int((int(str_array[str_counter])*-1) if (str_array[str_counter-1] == '-') else (str_array[str_counter]))
#   print(sum_array)

# productSum([5, 2, [7, -1], 3, [6, [-13, 8], 4]])

# METHOD 2 | RECURSION

def recurProductSum(arr, nest):
  sum = 0
  for item in arr:
    if(type(item) is list):
      sum += nest*recurProductSum(item, nest + 1)
    else:
      sum += nest*item 
  return sum 

def productSum(array):
  return (recurProductSum(array, 1))