# 75. Sort Colors

def sortColors(nums):
    i = 0
    while i < len(nums):
        print(nums,"->",i)
        n = nums[i]
        if n == 0 and i > 0:
            nums.pop(i)
            nums.insert(0,n)
            i += 1
        elif n == 2 and i <len(nums)-1:
            # check if there are all 2s
            if sum(nums[i:len(nums)]) == 2* (len(nums)-i):
                # all 2s
                break
            else:
                nums.pop(i)
                nums.append(n)
        else:
            i += 1

nums = [2,0,2,2,1,2,1,2,0,2,0,2,2,2]
sortColors(nums)
print(nums)