#leetcode 234. Palindrome Linked List
#https://leetcode.com/problems/palindrome-linked-list/
#연결리스트가 팰린드롬 구조인지 판별

from typing import List

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        q: List = []

        if not head:
            return True

        node = head

        while node is not None:
            q.append(node.val)
            node = node.next
        
        while len(q) > 1:
            if q.pop(0) != q.pop():
                return False

        return True

if __name__ == "__main__":
    f = [1, 2, 3, 6, 8, 10]
    print(f.pop(0))
    print(f.pop())
    print(f)