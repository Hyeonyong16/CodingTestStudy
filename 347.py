#leetcode 347. Top K Frequent Elemtns
#https://leetcode.com/problems/top-k-frequent-elements/
#k번 이상 등장하는 요소를 추출

import collections
import heapq
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = collections.Counter(nums)
        freqs_heap = []

        #heapq는 최소 힙을 지원하기때문에 음수로 해서 
        for f in freqs:
            heapq.heappush(freqs_heap, (-freqs[f], f))

        topk = list()
        for _ in range(k):
            topk.append(heapq.heappop(freqs_heap)[1])
                
        return topk
