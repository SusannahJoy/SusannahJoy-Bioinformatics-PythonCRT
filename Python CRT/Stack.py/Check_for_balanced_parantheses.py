class Stack:
    def __init__(self):
        self.Stack=[]
    def push(self,data):
        self.Stack.append(data)
        print(f"{data} Element is Appended")
    def isempty(self):
        if len(self.Stack)==0:
            return True
    def pop(self,data):
        if self.isempty():
            print("Stack is empty")
        else:
            self.Stack.pop()
            print(f"{data} Element is removed")
    def peek(self):
        Len=len(self.Stack)
        print(f"Peek element is {self.Stack[Len-1]}")
    def Display(self):
        self.Stack.reverse()
        for i in self.Stack:
            print(i)
    def Check_Balance(self):
        if '([{' in self.Stack:
            if self.Stack[3::]=='}])':
                print("Balanced Paranthesis")
        elif '({[' in self.Stack:
            if self.Stack[3::]==']})':
                print("Balanced Paranthesis")
        elif '{[(' in self.Stack:
            if self.Stack[3::]==')]}':
                print("Balanced Paranthesis")
        elif '{([' in self.Stack:
            if self.Stack[3::]=='])}':
                print("Balanced Paranthesis")
        elif '[{(' in self.Stack:
            if self.Stack[3::]==')}]':
                print("Balanced Paranthesis")
        elif '[({' in self.Stack:
            if self.Stack[3::]=='})]':
                print("Balanced Paranthesis")
        else:
            print("Imbalanced Paranthesis")
stack=Stack()
stack.push('([{}])')
stack.push('({[]})')
stack.push('{[()]}')
stack.push('{([])}')
stack.push('[{()}]')
stack.push('[({})]')
stack.Check_Balance()