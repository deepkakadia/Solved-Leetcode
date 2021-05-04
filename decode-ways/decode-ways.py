class Solution:
    def numDecodings(self, s: str) -> int:
        ans = 0
        @lru_cache(None)
        def rec(ind , s, ans ):
            if ind == len(s):
                return 1
            if s[ind] == "0":
                return 0
            if ind == len(s)-1:
                return 1
            ans = rec(ind+1,s,ans)
            if 10 <=int(s[ind:ind+2])<=26:
                ans+=rec(ind+2,s,ans)
            return ans
        
        return rec(0,s,ans)