#leetcode 706. Design HashMap
#https://leetcode.com/problems/design-hashmap/
#해시맵 구현하기

import collections
import hashlib

class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.table = collections.defaultdict(ListNode)
        
    #key값이 겹치면 값을 업데이트, 해시맵에 키, 값을 삽입
    def put(self, key: int, value: int) -> None:
        index = key % self.size
        if self.table[index].value is None:
            self.table[index] = ListNode(key, value)
            return
        
        #인덱스의 링크드리스트를 돌면서 key가 같은 값이 있는지 찾음
        p = self.table[index]
        while p:
            if p.key == key:
                p.value = value
                return
            #다 돌았는데 없으면 반복문 탈출
            if p.next is None:
                break
            #다음 노드로 넘어감
            p = p.next
        
        #같은 값이 없다는 것이므로 새로운 노드로 넣어줌
        p.next = ListNode(key, value)

    #key 에 해당하는 값을 조회, 없으면 -1 반환
    def get(self, key: int) -> int:
        index = key % self.size
        if self.table[index].value is None:
            return -1
        
        p = self.table[index]
        while p:
            #key 값이 같은 노드가 있으면 value를 반환
            if p.key == key:
                return p.value
            #다음 노드로 넘어감
            p = p.next
        
        return -1

    #key 값에 해당하는 값이 있으면 해시맵에서 삭제
    def remove(self, key: int) -> None:
        index = key % self.size
        if self.table[index].value is None:
            return

        #index의 첫번째 노드일때 삭제
        p = self.table[index]
        if p.key == key:
            self.table[index] = ListNode() if p.next is None else p.next
            return

        #연결리스트에 있으면 노드 삭제
        prev = p
        while p:
            if p.key == key:
                prev.next = p.next
                return
            prev, p = p, p.next