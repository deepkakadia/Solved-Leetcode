class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")":"(","]":"[","}":"{"}
        for x in s:
            if x in mapping:
                if mapping[x] != stack.pop() if stack else"#":
                    return False
            else:
                stack.append(x)
        return not stack