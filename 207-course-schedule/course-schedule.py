class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        coursedict = {}
        for i in range(len(prerequisites)):
            if prerequisites[i][1] not in coursedict:
                coursedict[prerequisites[i][1]] = [prerequisites[i][0]]
            else:
                coursedict[prerequisites[i][1]].append(prerequisites[i][0])
        
        #counting in degree
        indegree = [0]*numCourses
        for key in coursedict:
            for kids in coursedict[key]:
                indegree[kids] += 1
        queue = []
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)
        if len(queue) == 0:
            return False
        while queue:
            node = queue.pop(0)
            if node in coursedict:
                for kids in coursedict[node]:
                    indegree[kids] -= 1
                    if indegree[kids] == 0:
                        queue.append(kids)
        
        for i in indegree:
            if i !=0:
                return False
        return True
