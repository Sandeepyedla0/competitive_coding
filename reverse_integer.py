def revint(nums):
    rev_num=0
    m=nums
    if nums<0:
        nums=nums*-1
    while(nums>0):
        remainder=nums%10
        rev_num=(rev_num*10)+remainder
        nums=nums//10
    if(m<0):
        rev_num*=-1
    print(rev_num)


if __name__=="__main__":
    nums=-456
    revint(nums)