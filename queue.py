class Queue:
    def __init__(self):
        self.items = []


    def enqueue(self, item):
        self.items.append(item)


    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Dequeue from an empty queue")


    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())   # لازم 1 (أول واحد دخل)
print(q.size())      # لازم 2
print(q.is_empty())  # لازم False

# اختبار الحالة الفارغة
q.dequeue()
q.dequeue()
try:
    q.dequeue()
except IndexError as e:
    print("Caught:", e)