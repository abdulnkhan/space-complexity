class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
                *
            2       
        2,2    2,3
                 2,3,3
        
        [2,4,5,6]
        """
        res = []

        def dfs(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            if i > len(nums)-1 or total > target:
                return
            
            curr.append(nums[i])
            dfs(i, curr, total + nums[i])
            curr.pop()
            dfs(i+1, curr, total)


        dfs(0, [], 0)

        return res
        