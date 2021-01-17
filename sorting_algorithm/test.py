# recursion 

# f(x) = 2x + 3,    x = 1,2,3,4,......10 

# iteration 
def iteration():

    for x in range(1,11):
        result = 2 * x + 3
        print(result)

#iteration()


# recursion 

def recursion(x):
     
    if x < 11:

        result = 2 * x + 3
        print(result)
        recursion(x+1)

recursion(1)