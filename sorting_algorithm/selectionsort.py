
# time complexity => o(n^2) (best and worst case)
# space complexity => o(1)
def selectionsort():

    array_list = [40,20,60,10,50,30,2,9,44,70,1,3]
     
    array_list_len = len(array_list) 

    for i in range(0,array_list_len):

        min = i 

        for j in range (i+1,array_list_len):

            if array_list[min] > array_list[j]:

                min = j 

        # time for swapping 
        # satisfied the condition of swapping 
        if min != i:

            a = array_list[i]
            array_list[i] = array_list[min]
            array_list[min] = a  
    
    return array_list

if __name__ == "__main__":

    sorted_list = selectionsort()
    print(sorted_list)