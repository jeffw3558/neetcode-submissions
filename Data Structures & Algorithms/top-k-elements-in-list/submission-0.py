class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for i in nums:
            if i in count:
                count[i]+=1
            else:
                count[i]+=1
        return sorted(count, key=lambda x: count[x], reverse = True)[:k]
        

