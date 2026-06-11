class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        row={}

        for i in nums:
            row[i]=1+row.get(i,0)

        sorted_dict = dict(sorted(row.items(), key=lambda x:x[1], reverse=True))


        return list(sorted_dict.keys())[:k]
        