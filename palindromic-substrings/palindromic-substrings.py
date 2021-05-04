class Solution(object):
    def countSubstrings(self, s):
        n=len(s)
        ans=0
        for i in range(2*n -1):
            left= i//2
            right = left+ i%2
            while left>=0 and right<n and s[left]==s[right]:
                ans+=1
                left-=1
                right+=1
        return ans 
        