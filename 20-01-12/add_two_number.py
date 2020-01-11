
#https://leetcode.com/problems/add-two-numbers/solution/
#파이썬 모르는 개념 
#1. -> 솔직히 아직도 모르겠어요.
#2. map
#  * map() function returns 
    #a list of the results after applying 
    # the given function to each item of a given iterable.
# 3. [::-1] :역순으로 정렬해줌.
class Solution(object):
	def to_num(self, l1):
		n1 = 0
		mul = 1
		while l1 != None:
			n1 = l1.val * mul + n1
			mul *= 10
			l1 = l1.next
		return n1

	def addTwoNumbers(self, l1, l2):
		return map(int, str(self.to_num(l1) + self.to_num(l2))[::-1])
        return map(int, str(self.to_num(l1) +self.to_num(l2))[::-1])

#자바 
public class ListNode{
    int val;
    ListNode next;
    ListNode(int x) { val = x; }
}

class Solution{
    public ListNode addTwoNumbers(ListNode l1, ListNode l2){
        ListNode dummyHead = new ListNode(0);
        ListNode p = l1, q = l2, curr = dummyHead;
        int carry= 0;
        while (p != null || q != null){
            int x = (p != null) ? p.val : 0;
            int y = (q != null) ? q.val : 0;
            int sum = carry + x + y;
            carry = sum / 10;
            curr.next = new ListNode(sum % 10);
            curr = curr.next;
            if (p != null) p = p.next;
            if (q != null) q = q.next;
        }
        if (carry > 0){
            curr.next = new ListNode(carry);
        }
        return dummyHead.next;
    }
}