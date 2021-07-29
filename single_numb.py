
class solution:
    def __init__(self,nums):
        nums.sort()
        i=0
        l=len(nums)
        while(i<l-1):
            #print(i)
            if(nums[i]==nums[i+1]):
                i=i+2
            else:
                #print(nums[i])
                break
        print(nums[i])
    def sol(self,nums):
        bit = 0
        for num in nums:
            bit ^= num
            print("from bit",bit)
        print(bit)


if __name__=="__main__":
    nums=[1,2,2,4,4]
    cal=solution(nums)
    cal.sol(nums)