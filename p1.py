# 2. Two Sum
def twoSum(nums, target):
    for i in range(len(nums)):
        num = nums[i]
        o_num = target - num
        try:
            nums[i] = None
            oi = nums.index(o_num)
            return [i,oi]
        except:
            continue


a = [3,2,4]
b = 6
print(twoSum(a,b))