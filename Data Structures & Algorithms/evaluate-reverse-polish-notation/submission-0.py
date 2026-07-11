class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        

        for token in tokens:
            if token not in "+-*/":
                stack.append(int(token))

            else:
                a = stack.pop()
                b = stack.pop()
                result = int(eval(f"{b}{token}{a}"))
                stack.append(result)
        return stack[0]        