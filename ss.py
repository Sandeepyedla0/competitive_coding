def summm(nums):
    l=len(nums)
    temp=[]
    print(target)
    F=True
    for i in range(l-1):
        if(F==True):
            print("i here",i)
            for j in range(i+1,l):
                print("j here",j)
                if(nums[i]+nums[j]==target):
                    temp.append(i)
                    temp.append(j)
                    F==False
        else:
            break
    print(temp)


nums=[3,2,4]
target=6
summm(nums)