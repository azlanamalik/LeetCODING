# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        carry = 0

        dummy = ListNode(0)
        current = dummy

        while l1 is not None or l2 is not None or carry != 0:

            l1val = l1.val if l1 is not None else 0
            l2val = l2.val if l2 is not None else 0

            result = l1val + l2val + carry

            digit = result % 10
            carry = result // 10

            current.next = ListNode(digit)
            current = current.next

            if l1 is not None:
                l1 = l1.next

            if l2 is not None:
                l2 = l2.next

        return dummy.next
