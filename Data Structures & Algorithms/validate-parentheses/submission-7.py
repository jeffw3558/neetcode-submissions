class Solution:
    def isValid(self, s: str) -> bool:
        list = []
        for i in s:
            if i == "[" or i == "{" or i == "(":
                list.append(i)
            elif i == "]":
                if len(list) == 0 or list.pop() != "[":
                    return False
            elif i == "}":
                if len(list) == 0 or list.pop() != "{":
                    return False
            elif i == ")":
                if len(list) == 0 or list.pop() != "(":
                    return False
        return len(list) == 0

        
           