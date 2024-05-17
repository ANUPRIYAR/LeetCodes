class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key = lambda x: (x[0], -x[1]))

        n = len(envelopes)
        dp = []
        
        for w, h in envelopes:
            index = bisect_left(dp, h)
            # if the index is after the last element 
            # then append the element in dp, else replace 
            if index >= len(dp):
                dp.append(h)
            else:
                dp[index] = h

        return len(dp)
            
            
        