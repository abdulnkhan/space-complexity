class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lp = 0
        rp = len(numbers) - 1

        while lp < rp:
            sum = numbers[lp] + numbers[rp]
            if sum > target:
                rp -= 1
            elif sum < target:
                lp += 1
            else:
                return [lp+1, rp+1]
        return []