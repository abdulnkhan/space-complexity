class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
            preMap = {1:[2,3]}
            visit = set()
            dfs

        """

        preMap = {i:[] for i in range(numCourses)}
        visit = set()

        for crs, pre in prerequisites:
            preMap[crs].append(pre)

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
