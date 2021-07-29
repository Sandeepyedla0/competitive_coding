class solution:
    '''def __init__(self, prices):
        self.prices=prices
        profit=0
        for i in range(1,len(prices)):
            print(max(prices[i]-prices[i-1],0),"+",profit)
            profit+=max(prices[i]-prices[i-1],0)
            print(profit)'''

    def atmost_two(self, arr):
        profit=0
        m=max(arr)
        n=min(arr)
        print(m,n)
        for i in range(1,len(arr)-1):
            profit+=max(prices[i]-prices[i-1],0)

        print(arr)

if __name__=="__main__":
    prices=[3,3,5,0,0,3,1,4]
    cal=solution()
    cal.atmost_two(prices)
