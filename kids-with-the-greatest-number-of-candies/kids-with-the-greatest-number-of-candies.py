class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m  = max(candies)
        output = []
        for i in candies:
            output.append(bool(i+extraCandies >= m))
        return output
                
        