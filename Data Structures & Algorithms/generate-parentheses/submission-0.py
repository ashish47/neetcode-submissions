class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def makeB(o, c, cur):
            if o == n and c == n:
                res.append(cur)
                return
            if o == c:
                cur = cur + "("
                o += 1
            else:
                if o == n:
                    cur = cur + ")"
                    c += 1
                else:
                    makeB(o + 1, c, cur + "(")
                    cur = cur + ")"
                    c += 1
            
            makeB(o, c, cur)
        makeB(0, 0, "")
        return res