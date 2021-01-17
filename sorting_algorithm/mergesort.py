# merge sort (recursive way)

import math

def merging(mylist,l,h,mid):
    
    # get those data in two different list 
    list1 = mylist[l:mid+1]
    list2 = mylist[mid+1:h+1]
    
    # create a bigger number of that list 
    big_num = mylist[len(mylist) - 1] + 10 

    list1.append(big_num)
    list2.append(big_num)

    # l,h,mid all have the index value of mylist, so do not change the value 
    i = j = 0
    
    # i and j acts as a pointer but l and h are representing the index  
    for k in range(l,h+1):

        if list1[i] < list2[j]:

            mylist[k] = list1[i]

            i = i + 1
        else:

            mylist[k] = list2[j]

            j = j+1     


def mergesort(mylist,l,h): # l => low value of that array h=> high value of that array 
    
    
    if l < h:
      mid = math.floor((l + h)/2)
      mergesort(mylist,l,mid)
      mergesort(mylist,mid+1,h)
      merging(mylist,l,h,mid)

if __name__ == "__main__":

    mylist = [14,12,9,3,22,20,7,11,17,5]
    mylist_len = len(mylist) - 1

    mergesort(mylist,0,mylist_len)

    print(mylist)


