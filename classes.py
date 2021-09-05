class Base:
    def __init__(self):
        self.prop1 = "something1"
        self.__prop2 = "something2"

class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        print(self.prop1)
        print(self.__prop2)
obj1=Derived()
