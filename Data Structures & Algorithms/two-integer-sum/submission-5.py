class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_tracker = {}
        result = []
        for idx,ele in enumerate(nums):
            compliment = target - ele
        
            if compliment in index_tracker:
                return [index_tracker[compliment],idx]
            else:
                index_tracker[ele] = idx