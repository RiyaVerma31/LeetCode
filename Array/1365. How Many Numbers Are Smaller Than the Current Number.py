'''
https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
'''


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []
        count = 0
        for i in range(0, n):
            count = 0
            for j in range(0, n):
                if j != i and nums[j] < nums[i]:
                    count += 1
            ans.append(count)
        return ans

