'''
Write a python program to take the length of queue as input from the user 
and add the elements by using enqueue method and print the elements present in the queue 
and remove the elements one by one from the queue and check whether the queue is empty or not 
and print the front peek and rear peek
'''
from collections import deque
n=int(input("Enter the length of the Queue:"))
queue=deque()
for i in range(n):
    a=input("Enter the element:")
    queue.append(a)
print("Queue Elements:",queue)
print("Front Peek Elements:",queue[0])
print("Rear Peek Elements",queue[-1])
if not queue:
    print("Queue is Empty")
else:
    print("Queue is not Empty")
for i in range(len(queue)):
    queue.popleft()
    print("Dequeued Elements:",queue)