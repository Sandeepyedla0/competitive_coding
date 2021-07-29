class sol:
    def countandsay(self,n:int)->str:
        if(n==1):
            return("1")
        ct=1
        res=""
        prev=self.countandsay(n-1)
        #print(type(prev))
        print("previous",prev)
        for i in range(len(prev)):
            print("+++++i here++++++",i)
            if(i==len(prev)-1 or prev[i]!=prev[i+1]):
                res+=str(ct)+str(prev[i])
                print("present",res)
                ct=1
            else:
                ct+=1
        return(res)
if __name__=="__main__":
    n=4
    cal=sol()
    cal.countandsay(n)