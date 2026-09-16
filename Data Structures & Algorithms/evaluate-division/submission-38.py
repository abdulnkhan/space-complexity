class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = collections.defaultdict(list)

        for i, eq in enumerate(equations):
            a,b = eq
            adj[a].append([b, values[i]])
            adj[b].append([a, 1/values[i]])


        def bfs(src, target):
            if src not in adj or target not in adj:
                return -1

            q = deque()
            visit = set()
            q.append([src, 1])
            visit.add(src)

            while q:
                curr, w = q.popleft()
                if curr== target:
                    return w
                for child, multi in adj[curr]:
                    if child not in visit:
                        q.append([child, w*multi])
                        visit.add(child)

            return -1


        res = []

        for src, target in queries:
            res.append(bfs(src, target))

        return res