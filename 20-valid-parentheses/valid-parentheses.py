class Solution:
    def isValid(self, s: str) -> bool:
        mapOfBrckt = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        stck = []

        for bracket in s:
            if bracket in mapOfBrckt:
                stck.append(bracket)
            else:
                if not stck or bracket != mapOfBrckt[stck[-1]]:
                    return False

                stck.pop()

        return not stck