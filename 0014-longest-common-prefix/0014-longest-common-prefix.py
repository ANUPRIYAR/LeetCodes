class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()

        common = []
        first_str = strs[0]
        last_str = strs[-1]

        for i in range(len(first_str)):
            if i < len(last_str) and first_str[i] == last_str[i]:
                common.append(first_str[i])
            else:
                break

        return ''.join(common)
