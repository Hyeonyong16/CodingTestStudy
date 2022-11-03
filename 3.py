#leetcode 3. Longest Substring Without Repeating Characters
#https://leetcode.com/problems/longest-substring-without-repeating-characters/
#중복 문자가 없는 가장 긴 부분 문자열의 길이를 반환

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        max_length = start = 0

        for index, char in enumerate(s):
            if char in used and start <= used[char]:
                start = used[char] + 1
            else:
                #나까지 포함이니까 +1
                max_length = max(max_length, index - start + 1)
            
            used[char] = index
        
        return max_length