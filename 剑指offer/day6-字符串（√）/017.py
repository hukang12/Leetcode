from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return ""
        map_t = Counter(t)
        left = 0
        right = 0
        len_s = len(s)
        min_window = ""
        while left <= right < len_s:
            # 移动右指针
            while right < len_s:
                if s[right] in map_t:
                    map_t[s[right]] -= 1
                if max(list(map_t.values())) <= 0:
                    # 当前捕获的窗口
                    cur_window = s[left] if left == right else s[left:right + 1]
                    if min_window == "": min_window = cur_window
                    if len(cur_window) < len(min_window):
                        min_window = cur_window
                    # print(min_window)
                    break
                right += 1

            # 移动左指针，停止条件，max（map_t）=1且left指向的值在map_t
            while left <= right < len_s:
                if max(list(map_t.values())) == 1 and s[left] in t:
                    break
                if s[left] in map_t:
                    map_t[s[left]] += 1
                left += 1
                if max(list(map_t.values())) <= 0:
                    cur_window = s[left:right+1]
                    if len(cur_window) < len(min_window):
                        min_window = cur_window
                    # print(min_window)
            # 继续移动右指针
            right += 1
        return min_window




if __name__ == '__main__':
    so = Solution()
    s1 = input("s1:")
    s2 = input("s2:")
    res = so.minWindow(s1, s2)
    print("------\n", res)