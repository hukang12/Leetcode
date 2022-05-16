from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str):
        ans = []
        len_p, len_s = len(p), len(s)
        if len_p > len_s: return ans

        map_p = Counter(p)

        for i in range(len_p):
            if s[i] in map_p:
                map_p[s[i]] -= 1
            if max(list(map_p.values())) == 0:
                ans.append(0)

        for p in range(len_p, len_s):
            if s[p] in map_p:
                map_p[s[p]] -= 1
            if s[p - len_p] in map_p:
                map_p[s[p - len_p]] += 1
            if max(list(map_p.values())) == 0:
                ans.append(p - len_p + 1)

        return ans
if __name__ == '__main__':
    so = Solution()
    s1 = input("s1:")
    s2 = input("s2:")
    res = so.findAnagrams(s1, s2)
    print(res)

