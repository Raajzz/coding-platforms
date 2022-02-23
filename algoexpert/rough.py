

def sortedSquared(array):
    pos_pos = 0
    new_array = []
    for idx in range(len(array)):
        if(array[idx] >= 0):
            pos_pos = idx
        else:
            print("Hello")