class sol:
    def plusone(self,digits):
        #print(digits)
        res=""
        for i in range(len(digits)):
            res+=str(digits[i])
        res=int(res)+1
        print(res)
        res=list(int(x) for x in str(res))
        print(type(res))
        print(res)



if __name__=="__main__":
    digits=[9,9]
    cal=sol()
    cal.plusone(digits)
