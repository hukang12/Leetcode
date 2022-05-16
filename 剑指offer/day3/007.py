class Solution:
    """
    给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a ，b ，c ，使得 a + b + c = 0 ？请找出所有和为 0 且 不重复 的三元组。

    输入：nums = [-1,0,1,2,-1,-4]
    输出：[[-1,-1,2],[-1,0,1]]

    输入：nums = [0]
    输出：[]

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/1fGaJU
    """
    def threeSum(self, nums):
        nums.sort()
        arr_len = len(nums)
        if arr_len < 3:
            return []
        final = []
        for i in range(arr_len):
            num = nums[i]
            if i > 0 and num == nums[i-1]:
                continue
            two_sum = -num
            c = arr_len-1
            for b in range(i+1, arr_len):
                if b > i+1 and nums[b] == nums[b-1]:
                    continue
                while b<c and nums[b]+nums[c] > two_sum:
                    c -= 1
                if b == c:
                    break
                if nums[b]+nums[c] == two_sum:
                    final.append([num, nums[b], nums[c]])
        return final


if __name__ == '__main__':
    solu = Solution()
    arr_str = input("数组：\n").split()
    arr = [int(i) for i in arr_str]
    res = solu.threeSum(arr)
    print(res)
