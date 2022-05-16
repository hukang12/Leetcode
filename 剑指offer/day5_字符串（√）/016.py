class Solution:
    def lengthOfLongestSubstring(self, s) -> int:
        # if s==None:return 0
        s_len = len(s)
        if s_len ==1: return 1
        if s_len ==0: return 0
        left = 0
        right = 0
        longest_str = 0
        di = []
        while left<=right<s_len:
            while s[right] not in di:
                di.append(s[right])
                if right == s_len-1:
                    break
                right += 1
            cur_len = len(di)
            lap_char = s[right]

            if cur_len>longest_str:
                longest_str = cur_len

            while s[left] != lap_char:
                di.remove(s[left])
                left += 1
            di.remove(s[left])
            di.append(s[right])
            left += 1
            right += 1
        return longest_str

#"dsadfggfdgdsadasdsadsadadsadfggfdgdsadasdsadsadadsadfggfdgdsadasdsadsadadsadfggfdgdsadasdsadsadadsadfggfdgdsadasdsadsadadsadsadsadsadsadaewqrertyirtedsadfggfdgdsadasdsadsadadsadfggfdgdsadasdsadsadadsadfggfdgdsadasdsadsadadsadfggfdgdsadasdsadsadadsadfggfdgdsadasdsadsadadsadsadsadsadsadaewqrertyirtedsadfggfdgdsadasdsadsadadsadfggfdgdsadasdsadsadadsadfggfdgdsadasdsadsadadsadfggfdgdsadasdsadsadadsadfggfdgdsadasdsadsadadsadsadsadsadsadaewqrertyirtedsadfggfdgdsadasdsadsadadsadfggfdgdsadasdsadsadadsadfggfdgdsadasdsadsadadsadfggfdgdsadasdsadsadadsadfggfdgdsadasdsadsadadsadsadsadsadsadaewqrertyirtedsadfggfdgdsadasdsadsadadsadfggfdgdsadasdsadsadadsadfggfdgdsadasdsadsadadsadfggfdgdsadasdsadsadadsadfggfdgdsadasdsadsadadsadsadsadsadsadaewqrertyirtedsadfggfdgdsadasdsadsadadsadfggfdgdsadasdsadsadadsadfggfdgdsadasdsadsadadsadfggfdgdsadasdsadsadadsadfggfdgdsadasdsadsadadsadsadsadsadsadaewqrertyirte"
if __name__ == '__main__':
    str = input("字符串：\n")
    sl = Solution()
    res = sl.lengthOfLongestSubstring(str)
    print(res)