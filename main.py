class Solution:
    def __init__(self,passed_nums):
        self.nums=passed_nums
        i = 1
        l=len(nums)
        while(i<=l-2):
            if(nums[i]==nums[i-1]):
                del nums[i]
                i = i + 1
            else:
                i = i + 1
        print("sex",nums)

if __name__=="__main__":
    nums=[1,2,2,3,4,6,9,10,999,999]
    cal=Solution(nums)



