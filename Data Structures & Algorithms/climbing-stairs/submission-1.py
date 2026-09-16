class Solution:
    def climbStairs(self, n: int) -> int:
        """
        1d dynamic programing - loop through it n-1 times
        """
        one, two = 1, 1

        for i in range(n-1):
            temp = one
            one = one + two 
            two = temp

        return one
