# https://leetcode.com/problems/remove-nth-node-from-end-of-list/submissions/

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        out = None 
        vallist = []
        while True:
            vallist.append(head.val)
            head = head.next
            if head == None:
                break
        outlist= vallist[0:len(vallist)-n] + vallist[len(vallist)-n+1:]

        for i in range(len(outlist)-1, -1, -1):
            temp = ListNode(outlist[i])
            temp.next = out
            out = temp
        return out