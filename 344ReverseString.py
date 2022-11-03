#leetcode 344. Reverse String
#https://leetcode.com/problems/reverse-string/
#주어진 문자열을 뒤집는 함수
#입력값은 문자배열, 리턴없이 함수안에서 리스트 조작

from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1

        #투포인터를 이용
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        
        print(s)

if __name__ == "__main__":
    s = "anaconda"
    print(s[::-1])

    a = Solution()
    a.reverseString(["a","n","a","c","o","n","d","a"])