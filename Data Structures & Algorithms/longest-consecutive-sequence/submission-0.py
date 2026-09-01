class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        numset=set()
        largest=0
        for ele in nums:
            numset.add(ele)
        for ele in nums:
            if ele-1 in numset:
                pass
            elif ele-1 not in numset:
                count = 1
                val=ele
                while val in numset:
                    count+=1
                    val=val+1
                if count > largest:
                    largest = count
        return largest -1
                
                




                    

