class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_length=len(s)
        t_length=len(t)
        s_list=[]
        if s_length!=t_length:
            return False
        for i in s:
            s_list.append(i)
        for y in t:
            if y in s_list:
                s_list.remove(y)
            else: 
                return False
        return True
       
