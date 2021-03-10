class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        n = len(s)
        substringCount = collections.defaultdict(int)
        
        for index in range(n - minSize + 1):
            substring = s[index:index + minSize]
            
            if len(set(substring)) <= maxLetters:
                substringCount[substring] += 1
        
        return max(substringCount.values(), default=0)
        