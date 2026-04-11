class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hasher = {}
        for idx, sub in enumerate(nums):
            if target - sub in hasher:
                return [idx, hasher[target-sub]]
            hasher[sub] = idx