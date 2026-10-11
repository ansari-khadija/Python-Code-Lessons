# Method Overriding part_1

class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

Dog().sound()  # Bark


# Constructor Inheritance and Overriding part_2

class Parent:
    def __init__(self):
        print("Parent constructor")

class Child(Parent):
    pass

Child()


# super() Function part_3

class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greet(self):
        super().greet()
        print("Hello from Child")

Child().greet()


# Method Resolution Order (MRO) part_4


class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(B):
    pass

print(C.mro())
C().show()  # B


# Diamond Problem part_5


class A:
    def show(self):
        print("A")

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

D().show()
print(D.mro())