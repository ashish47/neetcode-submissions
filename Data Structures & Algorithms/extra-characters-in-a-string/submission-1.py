class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        """
        neetcodde

        """
        dp = {len(s): 0}
        def dfs(i):
            if i in dp:
                return dp[i]
            res = 1 + dfs(i + 1)
            for j in range(i, len(s)):
                for word in dictionary:
                    if s[i: i + len(word)] == word:
                        res = min(res, dfs(i + len(word)))
            dp[i] = res
            return res
        return dfs(0)