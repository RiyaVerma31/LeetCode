'''
https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
'''

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans = []
        n = len(candies)
        max_num = max(candies)
        for i in range(n):
            if (candies[i]+ extraCandies)  >= max_num:
                ans.append(True)
            else:
                ans.append(False)
        return ans