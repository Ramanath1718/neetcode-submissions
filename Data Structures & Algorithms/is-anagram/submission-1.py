class Solution:
    def isAnagram(self, t: str, x: str) -> bool:
        dict1 = {}
        dict2 = {}
        for i in range(len(t)):
            if t[i] in dict1:
                dict1[t[i]]+=1
            else:
                dict1[t[i]]=1
        for j in range(len(x)):
            if x[j] in dict2:
                dict2[x[j]]+=1
            else:
                dict2[x[j]]=1
        if dict1==dict2:
            return True
        return False
s1 = Solution()
print(s1.isAnagram("racecar","carrace"))