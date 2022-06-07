'''
https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/
'''


class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        ans = 0
        for sentence in sentences:
            words = sentence.split(' ')
            length_of_sentence = len(words)
            ans = max(ans, length_of_sentence)
        return ans

