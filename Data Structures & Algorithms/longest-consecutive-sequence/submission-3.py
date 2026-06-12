class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        sortNum=sorted(nums)
        has = defaultdict(list)
        res=[]
        res.append(sortNum[0])

        print(res)
        j=0

        for i in range(1,len(sortNum)):
            if(sortNum[i-1]==sortNum[i]-1):
                res.append(sortNum[i])
                print(res)
            elif(sortNum[i-1]==sortNum[i]):
                continue
            else:
                has[j].append(res)
                res = [sortNum[i]]
                j+=1

        has[j].append(res)

        maxi=0

        for i in range(len(has)):
            maxi = max(maxi, len(has[i][0]))

        return maxi

        