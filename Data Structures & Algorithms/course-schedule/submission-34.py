class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        preMap = {1: [2,3]}
        visit = set()

        dfs -> we just track if we're able to pop each pre-req - if we see that a node is already present in the visit set we know that there is a cyle that exists
        """

        preMap = {i:[] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visit = set()

        def dfs(crs):
            if preMap[crs] == []:
                return True

            if crs in visit:
                return False

            visit.add(crs)

            for pre in preMap[crs]:
                if not dfs(pre):
                    return False

            visit.remove(crs)
            preMap[crs] = []

            return True


        for crs in range(numCourses):
            if not dfs(crs):
                return False

        return True