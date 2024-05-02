class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        n  = len(arr)
        lengths = defaultdict(lambda:0)
        for num in arr:
            lengths[num] = lengths[num - difference] + 1
        return max(lengths.values())