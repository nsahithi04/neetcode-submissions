class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        Map=defaultdict(list)
        result=[]
        
        for i in strs:
            sorted_s=tuple(sorted(i))
            Map[sorted_s].append(i)

        for val in Map.values():
            result.append(val)

        return result