class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = {}
        
        for i in strs:
            sortstr = ''.join(sorted(i))
            if sortstr not in res:
                res[sortstr] = []
            res[sortstr].append(i)
        result = []
        for keys in res:
            result.append(res[keys])
        return result
        
