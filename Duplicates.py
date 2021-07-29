class solution:
    def dubp(self,nums):
        print(nums)
        l=len(nums)

        if (l%2 == 0):
            h = l // 2
        else:
            h = (l // 2)
        print("h",h)
        for i in range(0, h):
            k = i + 1
            while (k <= l - 1):
                print(i,k)
                if (nums[i] == nums[k]):
                    print(True)
                    break
                else:
                    k = k + 1

    def dup2(self,nums):
        nums.sort()
        l=len(nums)
        i=0
        while(i<=l-2):
            if(nums[i]==nums[i+1]):
                print(True)
                break
            elif(i==l-2):
                print("False")
                break
            else:
                i=i+1



if __name__=="__main__":
    nums=[14,22,18,32,12]
    cal=solution()
    #cal.dubp(nums)
    cal.dup2(nums)