class Solution:
    def validPalindrome(self, s) -> bool:
        len_s = len(s)
        left = 0
        right = len_s-1
        valid_del_num = 0
        while left <= right:
            if s[left] != s[right]:
                if left+1<len_s and s[left+1] == s[right]:
                    tmp_l = left+1
                    tmp_r = right
                    while tmp_l < tmp_r < len_s and s[tmp_l] == s[tmp_r]:
                        tmp_l += 1
                        tmp_r -= 1
                    if tmp_r == tmp_l or s[tmp_l] == s[tmp_r]:
                        valid_del_num = 1  # 左

                if right > 0 and s[left] == s[right-1]:
                    tmp_l = left
                    tmp_r = right - 1
                    while tmp_l < tmp_r < len_s and s[tmp_l] == s[tmp_r]:
                        tmp_l += 1
                        tmp_r -= 1
                    if tmp_r == tmp_l or s[tmp_l] == s[tmp_r]:
                        # right -= 1
                        valid_del_num = 1   # 右

                if valid_del_num == 1:
                    return True
                else:
                    return False
            left += 1
            right -= 1
        return True

if __name__ == '__main__':
    # "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"
    str = input("字符串：\n")
    sl = Solution()
    res = sl.validPalindrome(str)
    print(res)
