
def insertionsort(mylist):

    mylist_len = len(mylist)

    for pointer in range(1,mylist_len):
        
        position = pointer 

        while mylist[position] < mylist[position - 1] and position > 0:
             
             #swapping 
             a = mylist[position]
             mylist[position] = mylist[position - 1]
             mylist[position - 1] = a

             position = position - 1

    return mylist


def insertionsortOnline(data):

    mylist  = []
    mylist.append(data)
    mylist_len = len(mylist)

    for pointer in range(1,mylist_len):

        position = pointer

        while mylist[position] < mylist[position - 1] and position > 0:

            #swapping 
            a = mylist[position]
            mylist[position] = mylist[position - 1]
            mylist[position - 1] = a

            position = position - 1
    
    return mylist







