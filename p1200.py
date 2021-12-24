# 1200. Minimum Absolute Difference
class Solution:
    def minimumAbsDifference(self, arr):
        arr = sorted(arr)
        min_diff = 2*(10^6)
        return_arr = list()
        for i in range(1,len(arr)):
            diff = arr[i] - arr[i-1]
            if diff < min_diff:
                return_arr = []
                return_arr.append([arr[i-1], arr[i]])
                min_diff = diff
            elif diff == min_diff:
                return_arr.append([arr[i-1], arr[i]])
        return return_arr
arr = [4,2,1,3]
solution = Solution()
print(solution.minimumAbsDifference(arr))
