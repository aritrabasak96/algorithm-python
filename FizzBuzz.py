class FizzBuzz:
    def __init__(self):
        self.list = []
    def fizzbuzz(self,n):


        for i in range(1,n+1):
            if(i % 3 == 0):
              self.list.append("fizz")

            elif(i % 5 ==0):
              self.list.append("buzz")

            else:
              self.list.append(i)


    def printlist(self):
        for i in self.list:
           print(i)

if __name__ == "__main__":
    f = FizzBuzz()
    f.fizzbuzz(20)
    f.printlist()
