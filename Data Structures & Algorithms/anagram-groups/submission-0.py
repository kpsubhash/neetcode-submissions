from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        index_tracker = defaultdict(list)
        result = []
        for idx,ele in enumerate(strs):
            sorted_ele = "".join(sorted(ele))
            index_tracker[sorted_ele].append(ele)
        
        for value in index_tracker.values():
            result.append(value)
        return result

            

