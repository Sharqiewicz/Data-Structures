# About Stack
# LIFO
# peek allows us to look at the last item

def isEmpty(item):
    return len(item) > 0

class Stack():
    def __init__(self):
        self.stack = list()

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if isEmpty(self.stack):
            return self.stack.pop()
        else:
            return None

    def peek(self):
        if isEmpty(self.stack):
            return self.stack[len(self.stack) - 1]
        else:
            return None

    def __str__(self):
        return str(self.stack)