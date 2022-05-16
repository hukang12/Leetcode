class Solution:
    """
    给定一个已按照 升序排列  的整数数组 numbers ，请你从数组中找出两个数满足相加之和等于目标数 target 。
    函数应该以长度为 2 的整数数组的形式返回这两个数的下标值。

    输入：numbers = [1,2,4,6,10], target = 8
    输出：[1,3]
    解释：2 与 6 之和等于目标数 8 。因此 index1 = 1, index2 = 3 。

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/kLl5u1
    """
    def twoSum(self, numbers, target: int):
        last = None
        for i in range(len(numbers)):
            num = numbers[i]
            if num == last:
                continue
            else:
                last = num
            cha = target-num
            if cha in numbers[i+1:]:
                j = numbers.index(cha, i+1, len(numbers))
                return [i, j]


if __name__ == '__main__':
    arr_str = input("数组：\n").split()
    arr = [int(i) for i in arr_str]
    target = int(input("输入目标值\n"))
    solu = Solution()
    res = solu.twoSum(arr, target)
    print(res)