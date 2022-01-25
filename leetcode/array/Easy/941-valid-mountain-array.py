# METHOD 1 | 

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        count_up = 0
        count_down = 0
        if(len(arr)>=3):
            for i in range(0,len(arr)-1):
                if(arr[i] == arr[i+1]):
                    return False
                elif( (arr[i] < arr[i+1]) ):
                    if(count_down == 0):
                        count_up += 1
                    else:
                        return False
                elif( (arr[i] > arr[i+1]) ):
                    if(count_up >= 1):
                        count_down += 1
                    else:
                        return False
            if( (count_up>0) and (count_down>0) and (len(arr) == (count_up + count_down + 1) ) ):
               return True
            else:
               return False
        else:
            return False

# METHOD 2 | WOULD BE TO ITERATE THROUGH THE ARRAY TWICE, HAVE A DIFFERENT POINTER AT BOTH TIMES, SEE IF THE TWO POINTER MEET AT THE SAME POSIITON WHICH IS THE PEAK 