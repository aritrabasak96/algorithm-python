n = 20
my_list = [None] * n
print('first',my_list)

def randomHash(inp,n):

    hashValue = 0
    y = 0
    a = 1874563 # co-efficient
    c = 98

    for i in inp:
        hashValue = hashValue + ord(i)

    y = (a * hashValue) + c

    result = y % n

    return result

def anotherHash(inp,n):

    hashValue = 0

    for i in inp:

        hashValue = hashValue + ord(i)



    val = (hashValue * hashValue) + (3 * hashValue) + 12

    return val % n


def moduloHash(inp,n):

    hashValue = 0

    for i in inp:

        hashValue = hashValue + ord(i)

    result = hashValue % n

    return result

def hashValue(inp):

    hashValue = 0

    for i in inp:

        hashValue = hashValue + ord(i)


    return hashValue



def myFun():



    v1 = randomHash('aritra',n)
    my_list[v1] = 'aritra'
    v1_h = hashValue('aritra')
    print('hash',v1_h)
    print(v1)

    v2 = randomHash('debesh',n)
    my_list[v2] = 'debesh'
    v2_h = hashValue('debesh')
    print('hash',v2_h)
    print(v2)

    v3 = randomHash('souvik',n)
    my_list[v3] = 'souvik'
    v3_h = hashValue('souvik')
    print('hash',v3_h)
    print(v3)

    v4 = randomHash('mrinal',n)
    my_list[v4] = 'mrinal'
    v4_h = hashValue('mrinal')
    print('hash',v4_h)
    print(v4)

    v5 = randomHash('santonu',n)
    my_list[v5] = 'santonu'
    v5_h = hashValue('santonu')
    print('hash',v5_h)
    print(v5)

    v6 = randomHash('mou',n)
    my_list[v6] = 'mou'
    v6_h = hashValue('mou')
    print('hash',v6_h)
    print(v6)

    v7 = randomHash('amrita',n)
    my_list[v7] = 'amrita'
    v7_h = hashValue('amrita')
    print('hash',v7_h)
    print(v7)

    v8 = randomHash('rahul',n)
    my_list[v8] = 'rahul'
    v8_h = hashValue('rahul')
    print('hash',v8_h)
    print(v8)

    print(my_list)

if __name__ == "__main__":
    myFun()
