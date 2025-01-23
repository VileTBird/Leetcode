class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lp, rp = 0, len(numbers) - 1

        while lp < rp:
            currentNumber = numbers[lp] + numbers[rp]

            if (currentNumber < target):
                lp = lp + 1
            elif (currentNumber > target):
                rp = rp - 1
            else:
                return [lp + 1, rp + 1]
        