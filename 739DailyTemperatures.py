#leetcode 739. Daily Temperatures
#https://leetcode.com/problems/daily-temperatures/
#매일의 온도리스트를 받아서 더 따듯한 날씨를 위해서는 며칠을 기다려야 하는가

from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []

        for i, cur in enumerate(temperatures):
            while stack and cur > temperatures(stack[-1]):
                last = stack.pop()
                answer[last] = i - last
            stack.append(i)
        
        return answer
