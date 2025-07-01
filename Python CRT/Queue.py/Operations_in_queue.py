class Queue:
    def __init__(self):
        self.items=[]
    #Add items to rear(end)
    def enqueue(self,item):
        self.items.append(item)
    #Check Queue is Empty or not
    def is_empty(self):
        return len(self.items)==0
    #Remove and return front item
    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop(0)
    #Look at front item without removing
    def peek_front(self):
        if self.is_empty():
            return None
        #return self.items[0]
        else:
            R=self.items[0]
            print(R)
    #Look at rear item without removing
    def peek_rear(self):
        if self.is_empty():
            return None
        #return self.items[-1]
        else:
            r=self.items[-1]
            print(r)
    def size(self):
        return len(self.items)
Q1=Queue()
Q1.enqueue(3)
Q1.enqueue(4)
Q1.enqueue(5)
Q1.enqueue(6)
Q1.peek_front()
Q1.peek_rear()