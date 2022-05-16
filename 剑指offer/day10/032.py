class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        if s == t: return False
        diff = {}
        for i in range(len(s)):
            s_ch = s[i]
            if s_ch in diff:
                diff[s_ch] += 1
            else:
                diff[s_ch] = 1
            t_ch = t[i]
            if t_ch in diff:
                diff[t_ch] -= 1
            else:
                diff[t_ch] = -1
        print(diff)
        for k,v in diff.items():
            if v != 0:
                return False
        return True



if __name__ == '__main__':
    solu = Solution()
    s = input("s：\n")
    t = input("t：\n")
    res = solu.isAnagram(s, t)
    print(res)