class Solution:
    """左右两边子数组的和相等"""
    # 暴力
    def pivotIndex2(self, nums):
        for i in range(len(nums)):
            left = sum(nums[:i])
            right = sum(nums[i+1:])
            if left == right:
                return i
        return -1
    # 前缀和
    def pivotIndex(self, nums):
        pre_sum = 0
        all_sum = 0
        for num in nums:
            all_sum += num
        for i in range(len(nums)):
            right_sum = all_sum-pre_sum-nums[i]
            if pre_sum == right_sum:
                return i
            else:
                pre_sum += nums[i]
        return -1


if __name__ == '__main__':
    s = Solution()
    str = input("请输入数组：\n").split()
    arr = [int(a) for a in str]
    res = s.pivotIndex(arr)
    print(res)
