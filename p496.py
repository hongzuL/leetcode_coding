# 496. Next Greater Element I

def p496(nums1, nums2):
    next_gs = list()
    for n1 in nums1:
        n2si = nums2.index(n1)
        next_g = -1
        for n2i in range(n2si+1,len(nums2)):
            if n1 < nums2[n2i]:
                next_g = nums2[n2i]
                break
        next_gs.append(next_g)
    return next_gs

def main():
    nums1 = [2,4]
    nums2 = [1,2,3,4]
    ans = p496(nums1, nums2)
    print(ans)

main()