class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        stack = []
        result = []

        def helperfunc(opened, closed):
            if opened == closed == n:
                result.append("".join(stack))
                return

            if opened < n:
                stack.append("(")
                helperfunc(opened + 1, closed)
                stack.pop()

            if closed < opened:
                stack.append(")")
                helperfunc(opened, closed + 1)
                stack.pop()

        helperfunc(0, 0)
        return result