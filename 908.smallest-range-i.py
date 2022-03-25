#
# @lc app=leetcode id=908 lang=python3
#
# [908] Smallest Range I
#

# @lc code=start
class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        if len(nums) < 2:
            return 0
        nums = sorted(nums)
        return max(0, nums[-1] - nums[0] - 2 * k)
# @lc code=end

