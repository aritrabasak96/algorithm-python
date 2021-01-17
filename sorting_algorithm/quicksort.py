
# quicksort is works on divide and conquer strategy 

def partition(mylist,i,j):

    pivot = i 
    firstval=0
    lastvalue=0 

    # when j cross the array stop the array 
    while i < j:
         
        # increment i until you do not find a number greater than pivot 
        if firstval == 0:

           if mylist[i] > mylist[pivot]:
              firstval = 1
           else:
              i = i + 1
              firstval = 0
        

        if lastvalue == 0:
           # decrement j until you do not find a number smaller than pivot 
           if mylist[j] < mylist[pivot]:
              lastvalue = 1
           else:
              j = j - 1
              lastvalue = 0

        # we do have some data to swap
        if firstval != 0 and lastvalue != 0:

            # swap those value 
            a = mylist[i]
            mylist[i] = mylist[j]
            mylist[j] = a

            firstval = 0
            lastvalue = 0
    

    # once j crosses the i, swap the value 
    if j >= i:

        b = mylist[pivot]
        mylist[pivot] = mylist[j]
        mylist[j] = b 

    return j 

def quicksort(mylist,l,h):
    
    # l => first index h=> last index of the list 
    # when h crosses l the process is complete 
    if l < h:
        j = partition(mylist,l,h)
        quicksort(mylist,l,j)
        quicksort(mylist,j+1,h)  


if __name__ == "__main__":

    mlist = [12,3,44,9,17,6,2,10,13,6,7] 

    quicksort(mlist,0,len(mlist)-1)

    print(mlist)  



