'''
https://leetcode.com/problems/decompress-run-length-encoded-list/
'''

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums)
        for i in range(0, n, 2):
            temp_list = [nums[i+1]] * nums[i]
            ans = ans + temp_list
        return ans