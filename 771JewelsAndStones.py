#leetcode 771. Jewels and Stones
#https://leetcode.com/problems/jewels-and-stones/
#J가 보석 S가 돌일때 S에 보석이 몇개인가 (대소문자 구분)

import collections

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        result = collections.defaultdict(int)
        count = 0

        for char in stones:
            result[char] += 1

        for char in jewels:
            count += result[char]

        return count