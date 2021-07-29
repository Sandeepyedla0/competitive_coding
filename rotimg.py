class sol:
    def rot(self, matrix):
        self.matrix=matrix
        l=len(matrix)
        print(matrix)
        for i in range(l):
            for j in range(l):
                if(i!=j):
                    temp=matrix[i][j]
                    matrix[i][j]=matrix[j][i]
                    matrix[j][i]=temp
                else:
                    break
            print(matrix)
        for i in range(l):
            for j in range(l//2):
                temp=matrix[i][j]
                print("swaping",matrix[i][l-1-j],matrix[i][j])
                matrix[i][j]=matrix[i][l-1-j]
                matrix[i][l-1-j]=temp
if __name__=="__main__":
    matrix=[[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    cal=sol()
    cal.rot(matrix)
