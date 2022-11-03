#leetcode 125. Valid Palindrome
#https://leetcode.com/problems/valid-palindrome/
#주어진 문자열이 palindrome인지 구분하는문제
#대소문자 구분X 영문자와 숫자만을 대상

import collections
import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower() #대소문자를 구분하지 않으니 다 소문자로

        s = re.sub('[^a-z0-9]', '', s) #정규식을 이용하여 영어와 숫자를 제외하고는 필터링
        #sub => re.sub(대상, 새로운 것, 문자열)
        #'문자열'에서 '대상'을 '새로운 것' 으로 변경

        return s == s[::-1] #슬라이싱을 이용해 역순으로 만들어 둘이 같은지 비교



if __name__ == "__main__":
    a = Solution()
    result = a.isPalindrome("aAdCDaA")
    print(result)