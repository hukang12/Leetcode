
class Solution:
    """
    给定一个字符串数组 words，请计算当两个字符串 words[i] 和 words[j] 不包含相同字符时，它们长度的乘积的最大值。
    假设字符串中只包含英语的小写字母。如果没有不包含相同字符的一对字符串，返回 0。
    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/aseY1I
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    """
    def is_different(self, w1, w2):
        if len(w1) < len(w2):
            short_w = w1
            long_w = w2
        else:
            short_w = w2
            long_w = w1

        w1_char = set()
        for char in short_w:
            w1_char.add(char)
        for char in long_w:
            if char in w1_char:
                return False
        return True

    def maxProduct(self, words) -> int:
        max_res = 0
        word_num = len(words)
        for i in range(word_num-1):
            for j in range(i+1, word_num):
                if self.is_different(words[i], words[j]):
                    temp = len(words[i])* len(words[j])
                    if temp > max_res:
                        max_res = temp
        return max_res



if __name__ == '__main__':
    s = Solution()
    arr = input("输入字符串数组：\n").split()
    res = s.maxProduct(arr)
    print(res)
