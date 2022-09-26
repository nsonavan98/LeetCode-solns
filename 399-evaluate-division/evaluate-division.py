class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        
        adj_list = {}
        ###Fill the adj_list
        for i in range(len(equations)):
            for j in range(len(equations[0])):
                if equations[i][j] not in adj_list:
                    adj_list[equations[i][j]] = {}
                    
                if j == 0:
                    adj_list[equations[i][j]][equations[i][1]] = values[i]
                elif j==1:
                    adj_list[equations[i][j]][equations[i][0]] = (1/values[i])

        
        res = []
        
        def calcval(num,den,product,visited):      
            ### If number not in the adj list return -1
            
            if num not in adj_list or den not in adj_list:
                res.append(-1)
                return -1    
            if num == den:
                res.append(1)
                return 1
            if num not in visited:
                visited.add(num)
                #If den is present in num straight up return product
                if den in adj_list[num]:
                    product = product * adj_list[num][den]
                    res.append(product)
                    return product
                #Else loop in your childrens to find if you have the den
                else:
                    for node in adj_list[num]:
                        beforeres= len(res)
                        a = calcval(node,den,product*adj_list[num][node],visited) 
                        if len(res) >beforeres:
                            return a
        
        
        for num, den in queries:
            visited = set()
            beforelen = len(res)
            val = calcval(num,den,1,visited)
            if len(res) == beforelen:
                res.append(-1)
            
        return res
