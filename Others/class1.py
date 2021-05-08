class A:
    def __init__(self):
        self.__a = 15
    def display(self):
        print(self.__a,end=' ')

obj = A()
obj.display()
obj.__a = 20 #no update due to private var but also no error is shown
obj.display()