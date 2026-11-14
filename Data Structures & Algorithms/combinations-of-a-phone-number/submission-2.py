class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """

        """
        n_map = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        if not digits:
            return []
        def dfs(i):
            if i == len(digits):
                return [""]
            puch = []
            nxt = dfs(i + 1)
            print(i, nxt)
            for c in n_map[digits[i]]:
                for cur in nxt:
                    puch.append(c + cur)
            return puch
        return dfs(0)
            

