class A:
    def __init__(self, a, b, c):
        self.__a = a
        self._b = b
        self.c = c
    
    def display(self):
        print("Inside Class A Block...")
        print("a:", self.__a)
        print("b:", self._b)
        print("c:", self.c)

class B(A):
    def display(self):
        try:
            print("Inside Class B Block...")
            print("a:", self.__a)  # Raises exception when accessing private member
        except AttributeError:
            print("Private variable 'a' cannot be accessed...")
        print("b:", self._b)
        print("c:", self.c)

#Object created and used for calling respective functions
a=A(1, 2, 3)
a.display()

b=B(4, 5, 6)
b.display()