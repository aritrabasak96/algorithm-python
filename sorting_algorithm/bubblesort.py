

def bubblesort(mylist):
    
    k = len(mylist)
    pointer = 0

    while (pointer <= k):
       
      
       k = k - 1  
       
       for i in range(0,k):
          
         
          if mylist[i] > mylist[i + 1]:

              a = mylist[i]
              mylist[i] = mylist[i + 1]
              mylist[i + 1] = a

            


if __name__ == "__main__":

    mylist = [10,14,3,22,8,11,17,6,13]
    bubblesort(mylist)
    print(mylist)

