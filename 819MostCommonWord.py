#leetcode 819. Most Common Word
#https://leetcode.com/problems/most-common-word/
#금지된 단어를 제외한 가장 흔하게 등장하는 단어 출력
#대소문자 구분X, 구두점 무시, 대답은 소문자 반환

import collections
import re
from typing import List

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        #paragraph 문자열을 정규식을 통해 0-9a-zA-Z를 제외한 문자를 ' '로 변경
        #변경한 문자열을 lower를 통해 소문자로 변경한뒤 스플릿을 통해 리스트 생성
        #이 리스트에 단어가 banned에 있지 않으면 다시 원래 리스트에 대입

        #r프리픽스의 의미
        #\가 특수문자표현 용도가 아닌 순수하게 문자로 사용
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split()
        if word not in banned
        ]
        print(words)

        #collections를 이용, 각 문자가 문자열에서 몇번씩 나타나는지 알려주는 객체 생성
        counts = collections.Counter(words)
        print(counts)

        #가장 많이 나온 문자의 첫번째 인덱스 리턴(단어이름)
        return counts.most_common()[0][0]

if __name__ == "__main__":
    a = Solution()
    b = a.mostCommonWord("apple banana kang kang kang", ["apple", "kim"])
    print(b)