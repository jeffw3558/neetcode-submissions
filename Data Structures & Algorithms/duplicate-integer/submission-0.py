class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mouse=[]
        for i in nums:
            if i in mouse:
                return True
            else:
                mouse=mouse+[i]

        return False