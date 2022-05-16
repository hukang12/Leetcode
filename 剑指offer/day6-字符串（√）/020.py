class Solution:
    def is_hw(self, s):
        l=0
        r=len(s)-1
        while l<r:
            if s[l] != s[r]: return False
            l += 1
            r -= 1
        return True

    def countSubstrings(self, s) -> int:
        s_len = len(s)
        last_num = 0
        for i in range(s_len):
            for j in range(i+1):
                if self.is_hw(s[j:i+1]):
                    last_num += 1
        return last_num


if __name__ == '__main__':
    str = input("字符串：\n")
    sl = Solution()
    res = sl.countSubstrings(str)
    print(res)