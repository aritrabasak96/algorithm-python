# understand the recursion 

def recursion(x):

    if x > 4:

        recursion(x-1)
        recursion(x-2)
        printVal(x)

    
def printVal(x):

    print("from printval---",x)


if __name__ == "__main__":

    recursion(8)     