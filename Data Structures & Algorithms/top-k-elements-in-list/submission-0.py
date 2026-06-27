class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = {}
        output = []
        for i in nums:
            if i in result:
                result[i]+=1
            else:
                result[i]= 1
            
        sorted_item = sorted(result.items(), key = lambda x:x[1],reverse=True)

        for key,value in sorted_item[:k]:
            output.append(key)
        return output

        