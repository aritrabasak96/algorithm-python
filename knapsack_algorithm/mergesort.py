
import math 


def merging(mylist,l,h,mid):
    
    # get those data in two different list 
    list1 = mylist[l:mid+1]
    list2 = mylist[mid+1:h+1]
    
    # add a smaller number of that list 
    big_num = {'key':"k",'ratio':0,'weight':0}

    list1.append(big_num)
    list2.append(big_num)

    # l,h,mid all have the index value of mylist, so do not change the value 
    i = j = 0

    # i and j acts as a pointer but l and h are representing the index  
    for k in range(l,h+1):
        
        if float(list1[i]['ratio']) > float(list2[j]['ratio']):

            mylist[k] = list1[i]

            i = i + 1
        else:

            mylist[k] = list2[j]

            j = j+1     
        
    
def mergesort(mylist,low,high):
   
    
    if low < high:
 
        mid = math.floor((low + high)/2)

        mergesort(mylist,low,mid)
        mergesort(mylist,mid+1,high)
        merging(mylist,low,high,mid)
    
    return mylist 
    
