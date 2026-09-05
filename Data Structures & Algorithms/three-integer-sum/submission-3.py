class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        res = []
        for i in range(len(sorted_nums)-2):
            l,r = i+1, len(nums)-1
            if i > 0 and sorted_nums[i] == sorted_nums[i-1]: 
                continue
            while l<r:
                    if sorted_nums[i] + sorted_nums[l] + sorted_nums[r] == 0:
                        res.append([sorted_nums[i],sorted_nums[l],sorted_nums[r]])
                        while l<r and sorted_nums[l]==sorted_nums[l+1]:
                            l+=1
                        l+=1
                        r-=1
                    elif sorted_nums[i] + sorted_nums[l] + sorted_nums[r] < 0:
                        l+=1
                    elif sorted_nums[i] + sorted_nums[l] + sorted_nums[r] > 0:
                        r-=1    
            else:
                pass
            
        return res
            
            
        

