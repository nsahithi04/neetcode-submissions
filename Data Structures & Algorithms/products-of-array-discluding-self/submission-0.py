class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[1]*(len(nums))

        prefix=1
        for i in range(len(nums)):
           res[i]=prefix
           prefix=prefix*nums[i]

        print(res) 
            
        post=1
        for i in range(len(nums)-1,-1,-1):
            print(i)
            res[i]*=post
            post=post*nums[i]

        return res
