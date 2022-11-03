#leetcode 316. Remove Duplicate Letters.py
#https://leetcode.com/problems/remove-duplicate-letters/
#중복 문자 제거, 사전식 순서로 나열

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        for char in sorted(set(s)):
            suffix = s[s.index(char):]

            if set(s) == set(suffix):
                return char + self.removeDuplicateLetters(suffix.replace(char, ''))
        
        return ''