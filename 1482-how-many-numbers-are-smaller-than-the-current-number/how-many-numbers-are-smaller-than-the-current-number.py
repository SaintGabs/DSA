class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count = []
        counting = 0
        for i in range(len(nums)):

            for j in range(len(nums)):
                if nums[i] != nums[j] and nums[j] < nums[i]:
                    counting +=1
            count.append(counting)
            
            counting = 0

        return count