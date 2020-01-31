# Note: This Queue class is sub-optimal. Why?
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)


names = [
    {"first_name": "Margie"},
    {"first_name": "Belle"},
    {"first_name": "Andre"},
    {"first_name": "Jessi"},
    {"first_name": "Chrystal"},
    {"first_name": "Donny"},
    {"first_name": "Daniela"},
    {"first_name": "Engelbert"},
    {"first_name": "Vallie"},
    {"first_name": "Allyn"},
    {"first_name": "Hermon"},
    {"first_name": "Cynde"},
    {"first_name": "Albertine"},
    {"first_name": "Nahum"},
    {"first_name": "Thorny"},
    {"first_name": "Hadleigh"},
    {"first_name": "Sanson"},
    {"first_name": "Karmen"},
    {"first_name": "Kennett"},
    {"first_name": "Vito"},
    {"first_name": "Jemimah"},
    {"first_name": "Carrissa"},
    {"first_name": "Sanders"},
    {"first_name": "Aldus"},
    {"first_name": "Leontine"},
    {"first_name": "Kennedy"},
    {"first_name": "Valli"},
    {"first_name": "Bobbie"},
    {"first_name": "Launce"},
    {"first_name": "Hanni"},
]
