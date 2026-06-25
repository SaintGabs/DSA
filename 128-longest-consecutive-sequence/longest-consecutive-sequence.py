class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        MaiorSequencia = 0
        set_nums = set(nums)
        
        for i in set_nums:
            if i-1 not in set_nums:
                SequenciaAtual = 1
                while i+SequenciaAtual in set_nums:
                    SequenciaAtual+=1
                MaiorSequencia = max(MaiorSequencia, SequenciaAtual)
        return MaiorSequencia