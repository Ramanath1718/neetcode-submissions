class Solution:
    def topKFrequent(self, arr: List[int], k: int) -> List[int]:
        freq={}
        max=0
        k_elements=[]
        for val in arr:
            if val in freq:
                freq[val]+=1
            else:
                freq[val]=1
        sorted_freq = dict(sorted(freq.items(), key=lambda x: x[1],reverse=True))
        for i in sorted_freq:
            if len(k_elements)<k:
                k_elements.append(i)
        return k_elements
s1 = Solution()
print(s1.topKFrequent([7,7],1))