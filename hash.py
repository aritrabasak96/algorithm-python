
# take an input from the user

n = 10  # size of the table
my_list = [None] * n  # my list is fixed in size n = 10  this one is the data bucket


# this is simly the modulo hash function
def hashValue(inp): # the inp is the value
    hashASCII = 0
    map_value = 0

    # get the hash value
    for i in inp:
        hashASCII = hashASCII + ord(i)

    # the next thing is to map the value to a perticular range

    map_value = hashASCII % n
    print(inp,"hash value is",map_value)
    my_list[map_value] = inp

def print_list():
    return my_list


def getValue(inp):

    hashASCII = 0

    # get the hash value
    for i in inp:
        hashASCII = hashASCII + ord(i)

    # the next thing is to map the value to a perticular range

    map_value = hashASCII % 10
    print('map_value',map_value)
    return my_list[map_value]




if __name__ == "__main__":

     hashValue('aritra')
     hashValue('debseh')
     hashValue('souvik')
     hashValue('abhishek')
     hashValue('dibu')
     hashValue('santonu')
     hashValue('banti')
     hashValue('konkal')
     hashValue('gopal')
     hashValue('bama')
     hashValue('rahul')
     hashValue('sanu')

     v1 = print_list()
     print(v1)

     v =  getValue('aritra')
     print(v)
