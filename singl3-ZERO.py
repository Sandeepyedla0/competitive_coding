
class solution:
    def zer(self,nums):
        c = nums.count(0)
        nums=[i for i in nums if i!=0]
        print(type(nums))
        for i in range(c):
            nums.append(0)
        print(nums)
if __name__=="__main__":
    nums=[0,1,0,3,12]
    cal=solution()
    cal.zer(nums)