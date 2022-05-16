class Solution:
    """
    给定一个二进制数组 nums , 找到含有相同数量的 0 和 1 的最长连续子数组，并返回该子数组的长度。
    """
    def findMaxLength(self, nums):
        len_nums = len(nums)
        pre_dict = {0: -1}
        temp = 0
        max_len = 0
        for i in range(len_nums):
            temp = temp+1 if nums[i] else temp-1
            if temp in pre_dict.keys():
                temp_len = i-pre_dict[temp]
                max_len = max(temp_len, max_len)
            else:
                pre_dict[temp] = i
        return max_len


if __name__ == '__main__':
    s = Solution()
    str = input("请输入数组：\n").split()
    arr = [int(a) for a in str]
    res = s.findMaxLength(arr)
    print("----------\n", res)