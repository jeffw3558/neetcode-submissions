class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[]
        for i in range(len(nums)):
            total = 1
            for x in range(len(nums)):
                if x!=i:
                    total=total*nums[x]
                else:
                    pass
            res=res+[total]
        return res