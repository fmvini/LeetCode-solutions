# Last updated: 17/10/2026, 14:54:46
1class Solution:
2    def addTwoNumbers(self, l1, l2):
3        dummy = ListNode(0)
4        current = dummy
5        carry = 0
6
7        while l1 or l2 or carry:
8            x = l1.val if l1 else 0
9            y = l2.val if l2 else 0
10
11            total = x + y + carry
12            carry = total // 10
13            digit = total % 10
14
15            current.next = ListNode(digit)
16            current = current.next
17
18            if l1:
19                l1 = l1.next
20
21            if l2:
22                l2 = l2.next
23
24        return dummy.next