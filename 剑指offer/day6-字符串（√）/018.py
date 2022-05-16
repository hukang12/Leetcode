class Solution:
    def isPalindrome(self, s) -> bool:
        new_str = []
        for c in s:
            if c.isalpha() or c.isalnum():
                new_str.append(c.lower())
        len_str = len(new_str)
        start = 0
        end = len_str - 1
        while start <= end:
            if new_str[start] != new_str[end]:
                return False
            start += 1
            end -= 1
        return True


if __name__ == '__main__':
    str = input("字符串：\n")
    sl = Solution()
    res = sl.isPalindrome(str)
    print(res)