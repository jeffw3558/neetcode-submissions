class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        operand = []
        operator = {"+": lambda val2,val1: val1+val2, "-":lambda val2,val1: val2-val1, "*":lambda val2,val1: val2*val1, "/":lambda val2,val1: int(val2/val1)}
        for token in tokens:
            if token not in {"+","-","*","/"}:
                operand.append(int(token))
            else:
                val1 = operand.pop()
                val2 = operand.pop()
                result = operator[token](val2, val1)
                operand.append(result)

        return operand[0]

