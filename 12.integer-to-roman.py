# @before-stub-for-debug-begin
from python3problem12 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=12 lang=python3
#
# [12] Integer to Roman
#

# @lc code=start
class Solution:
    def intToRoman(self, num: int) -> str:
        numbers = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
        out_str = ""
        letter_dict = {1:'I',4:'IV',5:'V',9:'IX',10:'X',40:'XL',50:'L',90:'XC',100:'C',400:'CD',500:'D',900:'CM',1000:'M'}
        for n in range(len(numbers)-1,-1,-1):
            curr_num = numbers[n]
            multi_coe = num // curr_num
            out_str += multi_coe * letter_dict[curr_num]
            num -= multi_coe * numbers[n]
            
        return out_str
# @lc code=end

