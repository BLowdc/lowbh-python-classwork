class stack():
    def __init__(self, len) -> None:
        self.pointer = -1
        self.max = len
        self.stack = [None for i in range(len)]
    #end constructor

    def pop(self):
        if not self.isEmpty():
            data = self.stack[self.pointer]
            self.stack[self.pointer] = None
            self.pointer -= 1
            return data
        else:
            print("Stack is empty")
        #endif
    #endfunction

    def push(self, data) -> None:
        if not self.isFull():
            self.pointer += 1
            self.stack[self.pointer] = data
        else:
            print("Stack is full")
        #endif
    #endprocedure

    def peek(self):
        return self.stack[self.pointer]
    #endfunction

    def isFull(self) -> bool:
        return self.pointer == self.max - 1
    #endfunction

    def isEmpty(self) -> bool:
        return self.pointer == -1
    #endfunction

    def printStack(self) -> list:
        print("Stack:", end=' ')
        for elem in self.stack:
            if elem:
                print(elem, end=' ')
            #endif'
        #next elem
        print(' ')
#end class

myStack = stack(5)

myStack.push('apple')
myStack.push('banana')
myStack.push('oranges')
myStack.push('strawberry')
myStack.push('raspberry')
myStack.push('mango')
myStack.printStack()
print(myStack.peek())
print(myStack.pop())
print(myStack.peek())
print(myStack.pop())
print(myStack.pop())
print(myStack.pop())
print(myStack.pop())
print(myStack.pop())
myStack.printStack()






