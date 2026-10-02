class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        middle = int((right+left)/2)
        while right>=left:
            middle = int((right+left)/2)
            if nums[middle]>target:
                right = right-1
            elif nums[middle]<target:
                left = left+1
            elif nums[middle] == target:
                return middle
        return -1
            