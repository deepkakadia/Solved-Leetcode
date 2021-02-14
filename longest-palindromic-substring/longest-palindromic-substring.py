class Solution:
    
    def longestPalindrome(self, s: str) -> str:
        def check(s,l,r):
            if s ==None or l>r:
                return 0
            while l>=0 and r<len(s) and s[l]==s[r]:
                l-=1
                r+=1
            return r-l-1
        start = 0
        end = 0
        for i in range(len(s)):
            len1 = check(s,i,i)
            len2 = check(s,i,i+1)
            m = max(len1,len2)
            if m > (end-start):
                start = i - (m-1)//2
                end = i + (m//2)
        return s[start:end+1]
        
                