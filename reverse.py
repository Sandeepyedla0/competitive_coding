def rev(nums):
    for i in range(len(nums) - 1, -1, -1):
        print(nums[i], end=' ')
    temp=list(reversed(nums))
    print(temp)
    print(nums)



nums=[1,2,3,4,5]
rev(nums)