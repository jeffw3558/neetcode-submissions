class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            unique = [0]*26

            for c in s:
                unique[ord(c)-ord("a")]+=1
            res[tuple(unique)].append(s)
        return list(res.values())