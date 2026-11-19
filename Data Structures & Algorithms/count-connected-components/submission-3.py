class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        n = 5, edges = [[0,1],[1,2],[3,4]]
        0 -> 1
        0 ->
        2
        3 -> 4
        """

        class UnionSet:
            def __init__(self, n):
                self.parent = [i for i in range(n)]
                self.con_comp = n

            def getRoot(self, u):
                while u != self.parent[u]:
                    u = self.parent[u]
                return u

            def union(self, u, v):
                pu = self.getRoot(u)
                pv = self.getRoot(v)

                if pu != pv:
                    self.parent[pv] = u
                    self.con_comp -= 1
                

        g = UnionSet(n)    
        for u, v in edges:
            g.union(u, v)
        
        return g.con_comp

