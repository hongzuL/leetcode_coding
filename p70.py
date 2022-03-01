#70. Climbing Stairs
#You are climbing a stair case. It takes n steps to reach to the top.
class Solution:
    def climbStairs(self, n):
        steps = {}
        all_steps = self.climb(n, steps)
        return all_steps

    def climb(self, n, steps):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        if n in steps:
            return steps[n]
        one_step = self.climb(n-1, steps)
        two_step = self.climb(n-2, steps)
        all_step = one_step + two_step
        steps[n] = all_step
        return all_step
        

    def climb_table(self, n):
        table = [0]*n
        for i in range(n):
            if i == 0:
                table[i] = 1
            elif i == 1:
                table[i] = 2
            else:
                table[i] = table[i-1] + table[i-2]
        return table[n-1]

solution = Solution()
print(solution.climbStairs(3))