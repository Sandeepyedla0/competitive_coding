

class solution:
    def rot(self,nums,k):
        print(nums)
        print(k)
        l = len(nums)
        for i in range(k):
            print(i)
            temp = nums[l - 1]
            j = l
            while (j > 0):
                nums[j - 1] = nums[j - 2]
                j=j-1
            nums[0] = temp
        print(nums)
    def reverse(self, nums, start, end):
        print("now start and end=", start, end)
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            print("nums array is", nums)
            start, end = start + 1, end - 1
            print("now start and end=",start,end)


    def rotate(self, nums, k):
        n = len(nums)
        k %= n
        print(n)
        print(k)
        print("0ton-1")
        self.reverse(nums, 0, n - 1)
        print("0tok-1")
        self.reverse(nums, 0, k - 1)
        print("kton-1")
        self.reverse(nums, k, n - 1)
        print(nums)

if __name__=="__main__":
    nums=[1,2,3,4,5,6,7]
    k = 3
    cal=solution()
    cal.rotate(nums,k)