class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        Map=defaultdict(list)
        
        for i in strs:
            sorted_s=tuple(sorted(i))
            Map[sorted_s].append(i)

        return list(Map.values())