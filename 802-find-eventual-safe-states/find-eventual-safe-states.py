class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        
        #calculate outdegree
        #Add 0 outdegree in queue
        outdegree = [0]*len(graph)
        queue = []
        indict = {}
        for i in range(len(graph)):
            outdegree[i] = len(graph[i])
            if outdegree[i] == 0:
                queue.append(i)
        
        for i in range(len(graph)):
            indict[i] = []
            
        for i in range(len(graph)):
            for j in range(len(graph[i])):
                indict[graph[i][j]].append(i)
            
        res = []
        
        while queue:
            node = queue.pop(0)
            res.append(node)
            
            for innodes in indict[node]:
                outdegree[innodes] -= 1
                if outdegree[innodes] == 0:
                    queue.append(innodes)
        
        res.sort()
        return res
    
