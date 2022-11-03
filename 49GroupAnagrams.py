#leetcode 49. Group Anagrams
#https://leetcode.com/problems/group-anagrams/
#문자열 배열을 받아 애너그램 단위로 그룹

import collections
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #파이썬의 딕셔너리는 키/값 해시테이블 자료형
        anagrams = collections.defaultdict(list)

        for word in strs:
            #word의 단어를 sorted로 정렬, 정렬한걸 join으로 문자열로 연결
            #연결한 문자열을 키로 하여 딕셔너리에 추가
            #키값이 없을시 KeyError가 발생하므로 항상 디폴트를 생성해주는 defaultdict으로 생성
            anagrams[''.join(sorted(word))].append(word)

        #딕셔너리의 key말고 value값만 얻어서 리스트로 반환
        return list(anagrams.values())


if __name__ == "__main__":
    a = Solution()
    b = a.groupAnagrams(["apple", "banana", "tomato", "ppale"])
    print(b)