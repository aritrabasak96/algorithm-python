from linkedlist import Linkedlist

my_list = [None] * 10

link1 = Linkedlist()

my_list.insert(0,link1)
link1.insertData('abcd','good book',342)
val = my_list[0]
val.insertData('pqrs','bad book',455)


print(my_list[0].findData())

link2 = Linkedlist()

my_list.insert(1,link2)
link2.insertData('gif','not good',111)
