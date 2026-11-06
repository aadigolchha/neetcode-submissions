class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        self.visited = set()
        comps = 0

        nbrs = defaultdict(list)
        for node1, node2 in edges:
            nbrs[node1].append(node2)
            nbrs[node2].append(node1)

        for i in range(n):
            if i not in self.visited:
                self.dfs(nbrs, i)
                comps += 1
        return comps

    def dfs(self, nbrs, i):
        
        if i in self.visited:
            return

        self.visited.add(i)

        for nbr in nbrs[i]:
            if nbr not in self.visited:
                self.dfs(nbrs, nbr)
