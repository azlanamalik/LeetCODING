class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []

        def helper(current, opened, closed):

            if opened == closed == n:
                result.append(current)
                return

            if opened < n:
                helper(current + "(", opened + 1, closed)

            if closed < opened:
                helper(current + ")", opened, closed + 1)

        helper("", 0, 0)
        return result