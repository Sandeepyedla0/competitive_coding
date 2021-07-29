class sol:
    def fks(self,nums1, nums2):
        nums1.sort()
        nums2.sort()
        l1 = len(nums1)
        l2 = len(nums2)
        if l2>l1:
            nums2,nums1=nums1,nums2
            l1,l2=l2,l1
        i,j=0,0
        res=[]
        print(nums1)
        print(nums2)
        while(i<l1 and j<l2):
            if(nums1[i]==nums2[j]):
                #print(nums1[i])
                res.append(nums1[j])
                i+=1
                j+=1
            elif(nums1[i]>nums2[j]):
                j=j+1
            else:
                i=i+1
        print(res)
if __name__=="__main__":
    nums1=[3,1,2]
    nums2=[1,1]
    cal=sol()
    cal.fks(nums1,nums2)

