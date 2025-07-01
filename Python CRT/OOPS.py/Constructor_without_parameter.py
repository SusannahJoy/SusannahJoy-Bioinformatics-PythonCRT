#Constructor without parameter
class Mobile:
    def __init__(self):
        print("Mobile Constructor called")
realme=Mobile()
#another logic
class Mobile:
    #Constructor without parameter
    def __init__(self):
        self.model='RealMe X'
        self.model1='Samsung'
        self.model2='Vivo'
    def show_model(self):
        print("Model:",self.model)
        print("Model:",self.model1)
        print("Model:",self.model2)
realme=Mobile()
realme.show_model()