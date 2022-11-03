#leetcode 937. Reorder Log Files
#https://leetcode.com/problems/reorder-data-in-log-files/
#주어진 로그를 기준에 맞게 재정렬
#1. 로그의 가장 앞부분은 식별자
#2. 문자로 구성된 로그가 숫자 로그보다 앞
#3. 식별자는 순서에 영향X, 문자가 동일할 경우에는 식별자 순
#4. 숫자 로그는 입력 순서대로

from typing import List

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters, digits = [], []

        for log in logs:
            #식별자를 제외한 뒤부터 숫자인지 파악
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)
        
        #람다식을 이용해서 식별자 뒷부분부터 사전순 정렬, 같으면 식별자 순 정렬
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return letters + digits

if __name__ == "__main__":
    a = Solution()
    b = a.reorderLogFiles(["dif1 8 1 5 1", "a345 8 1 5 1", "a345 bert b c", "lef2 bert b c"])
    print(b)
