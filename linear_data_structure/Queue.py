class Queue():
    def __init__(self, _list=[]):
        _list.reverse()
        self.q = _list

    def enQueue(self, e):
        self.q.insert(0, e)

    def deQueue(self):
        return self.q.pop()

    def isEmpty(self):
        return self.q == []

    def size(self):
        return len(self.q)

    def __str__(self):
        return "size: " + str(self.size()) + ", current queue: " + str(self.q)


def test():
    my_queue = Queue([1,2,3,4,5])
    my_queue.enQueue(6)
    print(my_queue)
    my_queue.deQueue()
    print(my_queue)

    list1 = [1,2]
    list1+=[1,2]
    print(list1)

if __name__ == "__main__":
    test()
