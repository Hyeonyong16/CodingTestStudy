#leetcode 42. Trapping Rain Water
#https://leetcode.com/problems/trapping-rain-water/
#높이를 입력받아서 얼마나 많은 물이 쌓이는지 계산

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        volume = 0
        left, right = 0 , len(height) - 1
        left_max, right_max = height[left], height[right]

        while left < right:
            left_max, right_max = max(height[left], left_max), max(height[right], right_max)
            if left_max <= right_max:
                volume += left_max - height[left]
                left += 1
            else:
                volume += right_max - height[right]
                right -= 1
        
        return volume


if __name__ == "__main__":

    a = Solution()
    b = a.trap([1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])

    print(b)