class Graduation():
    def __init__(self):
        pass
    @staticmethod
    def Graduate():
        print("Congratulations you are a Graduate now")
#First Sub Class
class CSE(Graduation):
    def __init__(self):
        pass
    @staticmethod
    def Graduate():
        print("Congratulations you are a Computer Science Graduate now")
#Second Sub Class
class Bioinformatics(Graduation):
    def __init__(self):
        pass
    @staticmethod
    def Graduate():
        print("Congratulations you are a Bioinformatics Graduate now")
#Third Sub Class
class ECE(Graduation):
    def __init__(self):
        super().__init__()
    @staticmethod
    def Graduate():
        print("Congratulations you are a ECE Graduate now")
Graduation.Graduate()
CSE.Graduate()
Bioinformatics.Graduate()
ECE.Graduate()