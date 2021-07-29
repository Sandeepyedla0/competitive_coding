
def sol(nums1,nums2):
    l1 = len(nums1)
    l2 = len(nums2)
    temp = []
    if (l1 > l2):
        temp1 = set(nums1)
        temp=[value for value in nums1 if value  in nums2]
        print(temp)
nums1=[3,1,2]
nums2=[1,1]
sol(nums1,nums2)