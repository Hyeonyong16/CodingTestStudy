#leetcode 15. 3 Sum
#https://leetcode.com/problems/3sum/
#배열에서 합으로 0을 만들 수 있는 3개의 엘리먼트 출력

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            #i를 고정 i의 뒤에서 투포인터를 사용
            left, right = i + 1, len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum > 0:
                    right -= 1
                elif sum < 0:
                    left += 1
                else :
                    results.append((nums[i], nums[left], nums[right]))
                    #중복된 값은 나오면 안되니까
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

        return results

if __name__ == "__main__":
    a = Solution()
    b= a.threeSum([-1,0,1,2,-1,-4])
    print(b)
