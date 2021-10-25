# 1953. Maximum Number of Weeks for Which You Can Work
def numberOfWeeks(milestones):
    sum_mile = sum(milestones)
    max_mile = max(milestones)
    num_space = max_mile - 1
    if sum_mile - max_mile >= num_space:
        return sum_mile
    else:
        return sum_mile - max_mile + sum_mile - max_mile + 1

if __name__ == '__main__':
    milestones = [2,2,2]
    print(numberOfWeeks(milestones))
    