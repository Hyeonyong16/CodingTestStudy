#leetcode 1. Two Sum
#https://leetcode.com/problems/two-sum/
#타겟을 만들 수 있는 배열의 두 숫자 인덱스 리턴

from typing import List
import time

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        '''
        for i in range(len(nums)) :
            for j in range(i + 1, len(nums)) :
                if nums[i] == target - nums[j]:
                    return [i, j]
                    
        '''

        for i, n in enumerate(nums):
            print(i, n)
            complement = target - n
            if complement in nums[i + 1:] :
                return [nums.index(n), nums[i + 1:].index(complement) + (i + 1)]

if __name__ == "__main__":
    a = Solution()
    b= a.twoSum([1,2,5,9], 14)
    print(b)