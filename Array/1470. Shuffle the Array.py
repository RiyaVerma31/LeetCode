'''
https://leetcode.com/problems/shuffle-the-array/
'''


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        start_index = 0
        end_index = n
        ans = []

        while (start_index < n):
            ans.append(nums[start_index])
            ans.append(nums[end_index])

            start_index += 1
            end_index += 1

        return ans

