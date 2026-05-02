class Solution:
    def func(self,r:int, c:int):
        res=1
        for i in range(c):
            res=res*(r-i)
            res=res//(i+1)
        return res
    def generate(self, numRows: int) -> List[List[int]]:
        ans=[]
        for row in range(1,numRows+1):
            temp=[]
            for col in range(1,row+1):
                temp.append(self.func(row-1,col-1))
            ans.append(temp)
        return ans