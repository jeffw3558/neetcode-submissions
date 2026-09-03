class Solution:
    def isPalindrome(self, s: str) -> bool:

        curr=0
        end = len(s)-1


        while curr < end:
            if s[curr].isalnum() == False:
                curr+=1
            elif s[end].isalnum() == False:
                end-=1
            elif s[curr].lower() != s[end].lower():
                return False
            else:
                curr +=1
                end -=1
        return True
