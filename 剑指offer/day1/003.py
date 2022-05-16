"""
给定一个非负整数 n ，请计算 0 到 n 之间的每个数字的二进制表示中 1 的个数，并输出一个数组。

【示例】
输入: n = 5
输出: [0,1,1,2,1,2]
解释:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/w3tCBm
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


def countBits(n: int):
    res = []
    for i in range(n+1):
        count = 0
        while i:
            if i % 2 == 1:
                count += 1
            i = int(i/2)
        res.append(count)
    return res


if __name__ == '__main__':
    a = input("输入一个整数:\n")
    res = countBits(int(a))
    print(res)