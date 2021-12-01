# 198. House Robber
def rob(nums):
    if len(nums) <= 2:
        return max(nums)
    odd_house = list() # 1, 3 ...
    even_house = list() # 0, 2 ...
    if len(nums)%2 != 0:
        nums.append(0)
    if max(nums) == 0:
        return 0
    for i in range(len(nums)):
        if i%2 == 0:
            even_num = nums[i]
            even_house.append(even_num)
        else:
            odd_num = nums[i]
            odd_house.append(odd_num)
    print(even_house)
    print(odd_house)

    mix_profit = 0
    last_rob = 0
    last_profit = 0
    for j in range(1, len(even_house)):
        mix_profit -= last_profit
        # find the even profit
        even_profit = even_house[j-1]
        # find the odd profit
        odd_profit = odd_house[j-1]

        # find the current rob place
        if even_house[j] >= even_profit + odd_profit + odd_house[j]:
            # if the current added profit is larger than the even_profit + odd_profit, then it must be included
            mix_profit = rob(nums[0:2*j-1]) 
            last_profit = 0
            curr_profit = even_house[j]
            last_rob = 0
        else:
            # compare three cases
            case1 = even_house[j] + even_profit
            case2 = odd_house[j] + odd_profit
            case3 = odd_house[j] + even_profit
            print("---",j,"---")
            max_case = max(case1,case2,case3)
            if max_case == case1:
                curr_profit = even_house[j]
                if last_rob == 1:
                    # need to reconsider the previous choice
                    print("case1 meet")
                    old_profit = rob(nums[0:2*j-1]) 
                    print(old_profit + max(even_house[j],odd_house[j]),"|",mix_profit + case2)
                    
                    if old_profit + max(even_house[j],odd_house[j]) > mix_profit + case2:
                        mix_profit = old_profit
                        last_profit = 0
                        curr_profit = max(even_house[j],odd_house[j])
                        if max(even_house[j],odd_house[j]) == even_house[j]:
                            last_rob = 0
                        else:
                            last_rob = 1
                    else:
                        last_profit = odd_profit
                        curr_profit = odd_house[j]
                        last_rob = 1
                else:
                    last_profit = even_profit
                    last_rob = 0
            elif max_case == case2:
                curr_profit = odd_house[j]
                last_profit = odd_profit
                last_rob = 1
            else:
                curr_profit = odd_house[j]
                if last_rob == 1:
                    print("case3 meet")
                    # need to reconsider the previous choice
                    old_profit = rob(nums[0:2*j-1])
                    print(old_profit + max(even_house[j],odd_house[j]),"|",mix_profit + case2)
                    
                    if old_profit + max(even_house[j],odd_house[j]) > mix_profit + case2:
                        mix_profit = old_profit
                        last_profit = 0
                        curr_profit = max(even_house[j],odd_house[j])
                        if max(even_house[j],odd_house[j]) == even_house[j]:
                            last_rob = 0
                        else:
                            last_rob = 1
                    else:
                        last_profit = odd_profit
                        curr_profit = odd_house[j]
                        last_rob = 1
                else:
                    last_profit = even_profit
                    last_rob = 0
        print(mix_profit,"-> ", end="")
        mix_profit += curr_profit + last_profit
        print(last_profit, "+", curr_profit, "=", mix_profit)
        last_profit = curr_profit

    return mix_profit

        

# nums = [1,3,1,3,100]
nums = [6,3,10,8,2,10,3,5,10,5,3]
nums = [2,1,2,6,1,8,10,10]
# nums = [1]
# nums = [2,4,8,9,9,3]
# nums = [1,2,3,1]
# nums = [6,6,4,8,4,3,3,10]
# nums = [4,1,2,7,5,3,1]
nums = [104,209,137,52,158,67,213,86,141,110,151,127,238,147,169,138,240,185,246,225,147,203,83,83,131,227,54,78,165,180,214,151,111,161,233,147,124,143]
nums = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
nums = [1,1,1,1,1,1,1,1]
_output = rob(nums)
print(_output)
