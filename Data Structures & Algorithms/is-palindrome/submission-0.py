class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == None:
            return True
        new=""
        for ele in s:
            if ele.isalnum():
                new=new+ele.lower()
        if new == new[::-1]:
            return True
        return False