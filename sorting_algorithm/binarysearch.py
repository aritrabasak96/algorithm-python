# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and ru
# binary search algorithm 
import math
def binarySearch(data,point):

    first_point = 0
    second_point = len(data) - 1

    while first_point <= second_point: # first point should never exceed the last point or vice versa
        
        # the overall value like if a= 3.7 then a will become 4
        mid = math.ceil((first_point + second_point)/2)

        if data[mid] == point:
             
            return "found" 

        elif data[mid] < point:
            # the data must be in the right hand side
            first_point = mid + 1

        else:
            # left hand side 
            second_point = mid - 1

    return "not found"


if __name__ == "__main__":

    array = [3,7,9,12,17,19,23,29,34,37,42,46,48,52,55,59,62,65,69,70]
    input_value = int(input("what data you want to find"))
    
    
    result = binarySearch(array,input_value)
    print(result)
    
    
    
    
    