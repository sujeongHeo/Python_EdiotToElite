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
 '''
    1. (초기화) traversal <- 빈 리스트,  q <- 빈 큐
    2. 빈 트리가 아니면, root node 를 q 에 추가 (enqueue)
    3. q 가 비어 있지 않은 동안 
    3-1 node <- q에서 원소를 추출 
    3-2  node 를 방문 
    3.3 node 의 왼쪽, 오른쪽 자식 (있으면) 들을 q 에 추가
    4.  q 가 빈 큐가 되면 모든 노드 방문 완료
'''
    ####넓이 우선 순회 코드 과제  
    def bft(self):
        traversal = []  #1.
        q = ArrayQueue()
        if self.root:   #2.
            q.enqueue(self.root) #2
        while(q.isEmpty() == False): #3
            mov = q.dequeue() #3-1. 
            #  질문 : q.dequeue()가 실행 되고, 그 값이 mov 에 저장되는 것인가 ?
            traversal.append(mov.data)# 3-2
            if mov.left: #3-3
                q.enqueue(mov.left)
            if mov.right: #3-3
                q.enqueue(mov.right)
        return traversal


def solution(x):
    return 0
