class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        baixo=0
        alto=len(nums)-1
        pares = 0
        while baixo < alto:
            if nums[baixo] + nums[alto] < target:
                pares += alto - baixo
                baixo += 1
            else:
                alto -=1

        return pares
