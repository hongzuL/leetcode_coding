class Solution:
    def balancedStringSplit(self, s):
        b_count = 0
        lr_count = [0,0]
        i = 0
        while i < len(s):
            curr_s = s[i]
            if curr_s == "L":
                lr_count[0] += 1
            else:
                lr_count[1] += 1
            if lr_count[0] == lr_count[1]:
                b_count += 1
                lr_count = [0,0]
            i += 1
        return b_count
solution = Solution()
s = "RLRRRLLRLL"
print(solution.balancedStringSplit(s))
