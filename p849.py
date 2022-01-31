import math
from turtle import right
class Solution:
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        # idea is to find the max distance between two person or between person and each end
        max_num_seat_l = 0
        max_num_seat_r = 0
        left_end_dist = 0
        right_end_dist = 0
        left_end = 0
        right_end = len(seats) - 1
        for i in range(len(seats)):
            if seats[i] == 1:
                if i-left_end > max_num_seat_l:
                    max_num_seat_l = i-left_end
                left_end = i  
            else:
                if i == len(seats)-1:
                    # this is the right side seat
                    right_end_dist = len(seats)-1 - left_end
            if seats[len(seats)-1-i] == 1:           
                if right_end-(len(seats)-1-i) > max_num_seat_r:
                    max_num_seat_r = right_end-(len(seats)-1-i)
                right_end = len(seats)-1-i    
            else:
                if len(seats)-1-i == 0:
                    
                    # this is the left side seat
                    left_end_dist = right_end
            print(max_num_seat_l, max_num_seat_r, left_end_dist, right_end_dist)
        max_num_seat = max(max_num_seat_l, max_num_seat_r)
        return max(math.floor(max_num_seat/2), left_end_dist, right_end_dist)

seats = [1,0,0,0,0,0,0]
# seats = [0,1,1,0,1,1,0,1]
print(Solution().maxDistToClosest(seats))
        