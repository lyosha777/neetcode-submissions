class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1

        while (start < end):
            curr = numbers[start] + numbers[end]

            if curr > target:
                end -= 1

            elif curr < target:
                start += 1

            else:
                return [start + 1, end + 1]