class GrandFather():
    def __init__(self):
        pass
    #Method Overriding-same name,same parameters,same function but different class,implementation
    @staticmethod
    def Properties():
        print("100 Acres of Land")
class Father(GrandFather):
    def __init__(self):
        super().__init__()
    @staticmethod
    def Properties():
        print("50 Acres of Land")
class Yourself(Father):
    def __init__(self):
        super().__init__()
    @staticmethod
    def Properties():
        print("25 Acres of Land")
GrandFather.Properties()
Father.Properties()
Yourself.Properties()