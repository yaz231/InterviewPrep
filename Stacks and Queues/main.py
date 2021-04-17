class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def peek(self):
        return self.items[-1]

    def length(self):
        return len(self.items)

    def isEmpty(self):
        if self.length() == 0:
            return True
        return False

    def min(self):
        return min(self.items)

class Queue:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def remove(self):
        self.items.remove(0)

    def peek(self):
        return self.items[0]

    def length(self):
        return len(self.items)

    def isEmpty(self):
        if self.length() == 0:
            return True
        return False

def main():
    staxx = Stack()
    print(staxx.isEmpty())
    staxx.push(1)
    staxx.push(2)
    print(staxx.isEmpty())
    print(staxx.items)
    # staxx.pop()
    staxx.push(3)
    # staxx.pop()
    # staxx.pop()
    print(staxx.min())

    # q = Queue()
    # print(q.isEmpty())
    # q.add(0)
    # q.add(2)
    # print(q.isEmpty())
    # print(q.peek())
    # q.add(1)
    # q.remove()
    # print(q.items)

if __name__ == '__main__':
    main()