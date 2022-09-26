class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s)==1:
            return 1
        
        unique_set = set()
        left = 0

        maxlen = 0
        for i in range(len(s)):
            if s[i] not in unique_set:
                unique_set.add(s[i]) 
            else:
                maxlen = max(maxlen,len(unique_set)) 
                while(s[left] != s[i]):
                    unique_set.remove(s[left])
                    left+=1
                left+=1
        maxlen = max(maxlen,len(unique_set))
        return maxlen
                    
