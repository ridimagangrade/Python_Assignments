class Stack:
    def __init__(self):
        self.stack = []

    #Push element onto stack
    def push(self, item):
        self.stack.append(item)
        print(f"{item} pushed into the stack")

    # safe to pop
    def safe_pop(self):
        if len(self.stack) == 0:
            print("Stack is empty, nothing to pop")
            return None
        else:
            return self.stack.pop()
        
    # Display Stack
    def display(self):
        print("Stack", self.stack)

My_stack = Stack()

My_stack.push(10)
My_stack.push(20)
My_stack.push(30)

My_stack.display()

print("poped", My_stack.safe_pop())
print("poped", My_stack.safe_pop())
print("poped", My_stack.safe_pop())

# Trying to pop from empty stack
print("Poped: ", My_stack.safe_pop())
