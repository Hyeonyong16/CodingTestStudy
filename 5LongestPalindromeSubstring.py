#leetcode 5. Longest Palindrome Substring
#https://leetcode.com/problems/longest-palindromic-substring/
#가장 긴 팰린드롬 부분 문자열 출력

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left: int, right: int) -> str:
            while left >= 0 and right <= len(s) and s[left] == s[right-1]:
                left -= 1
                right += 1
            return s[left + 1:right - 1]
        
        if len(s) < 2 or s == s[::-1]:
            return s

        result = ''
        for i in range(len(s) - 1):
            result = max(result,
                         expand(i, i + 1),  #짝수개
                         expand(i, i + 2),  #홀수개
                         key=len)
        
        return result



if __name__ == "__main__":
    a = Solution()
    b = a.longestPalindrome("babad")
    print("final result:{}".format(b))