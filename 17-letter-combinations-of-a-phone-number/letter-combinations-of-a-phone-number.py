class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        d={2:'abc',3:'def',4:'ghi',5:'jkl',6:'mno',7:'pqrs',8:'tuv',9:'wxyz'}
        l=[]
        for i in digits:
            l.append(d.get(int(i)))
        curr=''
        ind=0
        res=[]
        def LCPhoneNum(l,curr,ind,res):
            if len(curr)==len(l) and curr!="":
                res.append(curr)
                return res
            if ind>=len(l):
                return res
            for i in range(len(l[ind])):
                curr=curr+l[ind][i]
                res=LCPhoneNum(l,curr,ind+1,res)
                curr=curr[0:ind]
            return res
        res=LCPhoneNum(l,curr,ind,res)
        return res
