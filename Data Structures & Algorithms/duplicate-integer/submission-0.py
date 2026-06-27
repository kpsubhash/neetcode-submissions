class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict1 = {}
        for num in nums:
            if num in dict1:
                return True
            else:
                dict1[num] = 1
        return False

# list1 = [1,2,3,5]
# Solution1 = Solution()
# print(Solution1.hasDuplicate(list1))
    

        