"""
给定两个 01 字符串 a 和 b ，请计算它们的和，并以二进制字符串的形式输出。
输入为 非空 字符串且只包含数字 1 和 0。

示例
输入: a = "1010", b = "1011"
输出: "10101"

https://leetcode-cn.com/problems/add-binary/
"""


class Solution:
    def addBinary(self, a: str, b: str):
        res = ""
        len_a = len(a)
        len_b = len(b)
        shorter = len_a if len_a < len_b else len_b     # 两个字符串中较短的一个
        shorter_id = 1 if len_a < len_b else 0

        carry_bit = 0   # 进位
        for i in range(shorter):
            cur_sum = int(a[len_a-i-1])+int(b[len_b-i-1])+carry_bit
            carry_bit = 1 if cur_sum > 1 else 0
            cur_res = cur_sum % 2
            res = str(cur_res)+res

        # 将多出的部分与进位相加
        rest_str = b if shorter_id else a
        rest_len = len(rest_str)-shorter
        for i in range(rest_len-1, -1, -1):
            temp_sum = int(rest_str[i])+carry_bit
            carry_bit = 1 if temp_sum > 1 else 0
            cur_res = temp_sum % 2
            res = str(cur_res) + res

        # 若进位还有1,则落下
        if carry_bit:
            res = "1"+res
        return res


if __name__ == '__main__':
    solu = Solution()
    input_str= input("请输入两个字符串：\n")
    a, b = input_str.split()
    res = solu.addBinary(a, b)
    print(res)