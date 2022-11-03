#leetcode 20. Valid Parenthese
#https://leetcode.com/problems/valid-parentheses/
#괄호가 올바르게 되있는지 판별

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        table = {
            ')' : '(',
            '}' : '{',
            ']' : '[',
        }

        #닫는 괄호일때 팝한 값
        for char in s:
            if char not in table:
                stack.append(char)
            elif not stack or table[char] != stack.pop():
                return False
        
        return len(stack) == 0