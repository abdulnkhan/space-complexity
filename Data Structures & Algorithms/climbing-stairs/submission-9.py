class Solution:
    def climbStairs(self, n: int) -> int:
        """
        [0,1,2,3,4]
        """

        one, two = 1,1

        for i in range(n-1):
            temp = one
            one += two
            two = temp

        return one