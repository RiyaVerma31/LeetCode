'''
https://leetcode.com/problems/richest-customer-wealth/
'''


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for x in accounts:
            _sum = 0
            for y in x:
                _sum = _sum + y
            if _sum > max_wealth:
                max_wealth = _sum
        return max_wealth
