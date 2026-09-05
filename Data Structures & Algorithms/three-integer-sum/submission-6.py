class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        for i, val in enumerate(nums):

            l,r = i+1, len(nums)-1

            if i>0 and val == nums[i-1]:
                continue

            while l<r:
                ThreeSum = val + nums[l] + nums[r]
                if ThreeSum > 0:
                    r-=1
                elif ThreeSum < 0:
                    l+=1
                elif ThreeSum == 0:
                    res.append([val, nums[l],nums[r]])
                    l+=1
                    r-=1
                    while r>l and nums[l] == nums[l-1]:
                        l+=1
                    while r>l and nums[r] == nums[r+1]:
                        r-=1

        return res
            
            
        

