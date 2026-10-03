class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        
        self.items.append(item)

    def pop(self):
       
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from empty stack")

    def peek(self):
        
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("peek from empty stack")

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
    
def reverse_word(word):
    stack = Stack()
    for char in word:
      stack.push(char)
      reversed_word = ""
    while not stack.is_empty():
            reversed_word += stack.pop()
    return reversed_word


s = Stack()
print(reverse_word("hello"))  # لازم "olleh"