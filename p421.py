# 421. Maximum XOR of Two Numbers in an Array
class Solution:
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # a ^ b = c
        # a ^ c = b
        # b ^ c = a
        # candiate is the estimate of the maximum XOR, and we are finding if the c ^ b = a
        max_num = 0
        for i in range(32)[::-1]:
            max_num *= 2#max_num <<= 1 # in order to be the same length with the longest number
            prefixes = set(num >> i for num in nums) 
            
            candidate = max_num + 1
            for p in prefixes:
                if candidate ^ p in prefixes:
                    max_num = candidate
                    break
            print(candidate, prefixes, max_num)
        return max_num

solution = Solution()
nums = [3, 10, 5, 25, 2, 8]
# nums = [14,70,53,83,49,91,36,80,92,51,66,70]
print(solution.findMaximumXOR(nums))