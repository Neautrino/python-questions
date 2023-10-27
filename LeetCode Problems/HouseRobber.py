# 198. House Robber
# https://leetcode.com/problems/house-robber/description/
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        dp = [0]*(len(nums)+1)
        dp[1]=nums[0]
        for i in range(1,len(nums)):
            val = nums[i]
            dp[i+1] = max(dp[i],dp[i-1]+val)
        return dp[len(nums)]




        
