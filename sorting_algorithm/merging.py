# combining two sorted list into one single sorted list 
# ex: list1 = [2,6,8,9,12,17,22,27,32]
#     list2 = [3,9,11,16,19,24]
#     result = [2,3,6,8,9,9,11,12,16,17,19,22,24,27,32]
def merging(list1,list2):

    cursor_list1 = 0 # always start from 0 index 
    cursor_list2 = 0 

    list1_size = len(list1) - 1   # get the size of both list 
    list2_size = len(list2) - 1   

    result_list = [] # empty list where we add our result 
    
    # the while loop will continue until the cursor not reached at the end of those list 
    while cursor_list1 <= list1_size and cursor_list2 <= list2_size:
         
        list1_data = list1[cursor_list1]
        list2_data = list2[cursor_list2]
            
        # list one data is smaller than list two data 
        if list1_data < list2_data:

            result_list.append(list1_data)
            cursor_list1 = cursor_list1 + 1

        elif list1_data > list2_data:

            result_list.append(list2_data)
            cursor_list2 = cursor_list2 + 1

        elif list1_data == list2_data:
            
            #choose anything
            result_list.append(list2_data)
            cursor_list2 = cursor_list2 + 1           

    # loop through it if any data remaining 
    for p1 in range(cursor_list1,list1_size+1):
        result_list.append(list1[p1])

    for p2 in range(cursor_list2,list2_size+1):
        result_list.append(list2[p2])

    return result_list        

if __name__ == "__main__":

    list1 = [2,6,8,12,17,22,27,31]
    list2 = [3,9,11,16,19,24,27,29,32,33]

    result = merging(list1,list2)
    
    print(result)



