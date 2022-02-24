# METHOD 1 | LOOP THROUGH ARRAY INCREMENT SUB-SEQUENCE

def isValidSubsequence(array, sequence):
    
    ptr_sub = 0

    for value in array:
        if(value == sequence[ptr_sub]):
            ptr_sub += 1
            if(ptr_sub == len(sequence)):
                return True

    return False

print (isValidSubsequence([1,2,3,4], [1,2]))


# METHOD 2 | similar, instead of comparing everytime, we can have a try..except where if we go to the except block we'll return true, if not then finally we'll return False (for brevity).