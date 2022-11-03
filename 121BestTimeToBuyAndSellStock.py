#leetcode 121. Best Time to Buy and Sell Stock
#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
#한번의 거래로 낼 수 있는 최대 이익

from typing import List
import sys

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = sys.maxsize

        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)

        return profit

if __name__ == "__main__":
    a = Solution()
    b= a.maxProfit([1,4,3,6,2])

    print(b)
