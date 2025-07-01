from collections import deque
stack=deque()
stack.append('A')
stack.append('B')
stack.append('C')
print("Stack after pushing:",stack)
top=stack.pop()
print("Popped element:",top)
print("Stack after popping",stack)
if not stack:
    print("Stack is empty")
else:
    print("Stack is not empty")
print("Top element:",stack[-1])