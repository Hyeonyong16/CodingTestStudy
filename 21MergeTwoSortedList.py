#leetcode 21. Merge Two Sorted List
#https://leetcode.com/problems/merge-two-sorted-lists/
#정렬되어 있는 두 연결 리스트 합치기

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        #list1이 없거나 list2가 있고 list1의 val값이 list2 보다 크면
        #두 노드를 바꾸어준다.
        if (not list1) or (list2 and (list1.val > list2.val)):
            list1, list2 = list2, list1
        #작은값을 가진 노드를 계속 list1에 넣기때문에
        #list2의 값이 list1보다 큼
        #이를 반복
        #마지막엔 None이니까 list2에 남은 마지막 노드는 맨 뒤에 붙게됨
        if list1:
            list1.next = self.mergeTwoLists(list1.next, list2)
        return list1