class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key = lambda x: x[1])
        count = 0
        curr = float('-inf')
        for start, end in pairs:
            if start > curr:
                curr = end
                count += 1
            elif start < curr and end < curr:
                curr = end
        return count
