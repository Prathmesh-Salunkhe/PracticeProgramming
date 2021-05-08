class A:
    def __init__(self, val1):
        self.value = val1

    def method_a(self):
        print(self)
        return 20 + self.value


class B(A):
    def __init__(self, val2):
        self.num = val2

    def method_b(self, b):
        super().__init__(100)  # here the self is b, so the init func of Class A has self = b ,so b.value = 100 not a.value = 20
        return self.method_a() + self.num


a = A(20)
b = B(10)
print(b.method_b(a))
