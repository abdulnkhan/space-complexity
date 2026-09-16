class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = collections.defaultdict(list)
        for i, eq in enumerate(equations):
            adj[eq[0]].append([eq[1], values[i]])
            adj[eq[1]].append([eq[0], 1/values[i]])

        def bfs(src, target):
            if src not in adj.keys() or target not in adj.keys():
                return -1

            q = deque()
            q.append([src, 1])
            visit = set()
            visit.add(src)

            while q:
                node, w = q.popleft()
                if target == node:
                    return w
                for neigh, multi in adj[node]:
                    if neigh not in visit:
                        q.append([neigh, w*multi])
                        visit.add(neigh)
            return -1

            
        res = []
        for src, target in queries:
            res.append(bfs(src, target))
        
        return res

