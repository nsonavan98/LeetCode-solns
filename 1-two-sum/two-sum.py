class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        numdict = {}
        
        for i in range(len(nums)):
            if nums[i] not in numdict:
                numdict[target-nums[i]] = i
            else: 
                print(numdict)
                return [i,numdict[nums[i]]]
