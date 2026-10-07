class Solution:
    def trap(self, height: List[int]) -> int:
        # min of Right and left - height of index i

        n = len(height)
        maxLeft = [0]*n
        maxRight = [0]*n
        minVal = [0]*n
        total = 0
        for i in range(0,len(height)):
            if i == 0: 
                maxLeft[0] = height[i]
            maxLeft[i]= (max(height[i],maxLeft[i-1]))
        r=len(height)-1
        while r > -1:
            if r == len(height)-1:
                maxRight[r] = height[r]
                r-=1
            else:
                maxRight[r] = max(height[r],maxRight[r+1])
                r-=1
        for ele in range(0,len(height)):
            minVal[ele] = min(maxRight[ele],maxLeft[ele])
        for _ in range(0,len(height)):
            total += max(0, minVal[_]-height[_])
        return total
                

            
        