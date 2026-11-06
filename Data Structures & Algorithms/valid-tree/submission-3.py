class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if n == 1:
            return True

        if len(edges) != n-1:
            return False

        nbrs = defaultdict(list)
        for node1, node2 in edges:
            nbrs[node1].append(node2)
            nbrs[node2].append(node1)

        visited = set()
        q = deque()
        q.append(0)

        while q:
            for i in range(len(q)):
                curr = q.popleft()

                for nbr in nbrs[curr]:
                    if nbr not in visited:
                        visited.add(nbr)
                        q.append(nbr)

        return len(visited) == n
