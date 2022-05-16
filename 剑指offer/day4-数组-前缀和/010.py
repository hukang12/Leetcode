class Solution:
    def subarraySum(self, nums, k) -> int:
        count = 0
        arr_len = len(nums)
        pre_sum = 0
        pre_dict = {0: 1}
        for i in range(arr_len):
            pre_sum += nums[i]
            if pre_sum-k in pre_dict.keys():
                tmp = pre_dict[pre_sum-k]
                count += tmp

            if pre_sum not in pre_dict.keys():
                pre_dict[pre_sum] = 1
            else:
                pre_dict[pre_sum] += 1
        return count


if __name__ == '__main__':
    s = Solution()
    str = input("请输入数组：\n").split()
    arr = [int(a) for a in str]
    k = int(input("输入K:\n"))
    res = s.subarraySum(arr, k)
    print("----------\n", res)