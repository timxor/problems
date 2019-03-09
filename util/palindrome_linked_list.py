# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:

        # stack, lifo, list in python
        # stack = []
        stack = []

        pointer = head

        while pointer != None:
            stack.append(pointer.val)
            print(pointer.val)
            pointer = pointer.next

        pointer = head
        while len(stack) > 0:
            index = stack.pop()
            print("index = ", index)
            print("pointer.val = ", pointer.val)

            # compare for equality
            if index != pointer.val:
                return False
            print(index == pointer.val)
            pointer = pointer.next

        return True


# Input: 1->2
# Output: false
