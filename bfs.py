###  ArrayQueue 는 제공되어 있는 코드 #######
class ArrayQueue:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def enqueue(self, item):
        self.data.append(item)

    def dequeue(self):
        return self.data.pop(0)

    def peek(self):
        return self.data[0]


class Node:

    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None


class BinaryTree:

    def __init__(self, r):
        self.root = r
 
    ####넓이 우선 순회 코드 과제  
    def bft(self):
        traversal = []
        q = ArrayQueue()
        if self.root:
            q.enqueue(self.root)
        while(q.isEmpty() == False):
            mov = q.dequeue() ###q.dequeue()가 실행 되고, 그 값이 mov 에 저장되는 것인가 ?
            traversal.append(mov.data)
            if mov.left:
                q.enqueue(mov.left)
            if mov.right:
                q.enqueue(mov.right)
        return traversal


def solution(x):
    return 0
