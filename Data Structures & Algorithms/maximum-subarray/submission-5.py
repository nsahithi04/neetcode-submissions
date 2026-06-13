class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsub=nums[0]
        sub=nums[0]

        for i in range(1,len(nums)):
            if(sub<0):
                sub=nums[i]
            elif(sub>=0):
                sub+=nums[i]
            maxsub=max(sub,maxsub)

    
        return maxsub