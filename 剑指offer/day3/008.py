import bisect


class Solution:
    def minSubArrayLen(self, target: int, nums):
        # 暴力破解——超时
        min_arr_len = len(nums)
        arr_sum = 0
        for n in nums:
            arr_sum += n
        if arr_sum < target:
            return 0
        for i in range(len(nums)):
            num = nums[i]
            target_idx = i+1
            cur_sum = num
            while cur_sum < target and target_idx < len(nums):
                cur_sum += nums[target_idx]
                target_idx += 1
            if cur_sum >= target and target_idx-i < min_arr_len:
                min_arr_len = target_idx-i

        return min_arr_len

    # 滑动窗口
    def minSubArrayLen_windows(self, target: int, nums):

        # 213
        # [12,28,83,4,25,26,25,2,25,25,25,12]
        min_arr_len = len(nums)
        start = 0
        end = 0
        cur_sum = 0
        flag = False
        while end < len(nums):
            while cur_sum < target and end < len(nums):
                cur_sum += nums[end]
                end += 1
            if cur_sum >= target:
                flag = True
                while start <= end and cur_sum >= target:
                    cur_sum -= nums[start]
                    start += 1
                cur_len = end-start+1
                if cur_len < min_arr_len:
                    min_arr_len = cur_len

        return min_arr_len if flag else 0

    # 前缀+二分查找
    def minSubArrayLenBisect(self, s, nums):
        if not nums:
            return 0

        n = len(nums)
        ans = n + 1
        sums = [0]
        for i in range(n):
            sums.append(sums[-1] + nums[i])

        for i in range(1, n + 1):
            target = s + sums[i - 1]
            bound = bisect.bisect_left(sums, target)
            if bound != len(sums):
                ans = min(ans, bound - (i - 1))

        return 0 if ans == n + 1 else ans


if __name__ == '__main__':
    solu = Solution()
    arr_str = input("数组：\n").split()
    arr = [int(i) for i in arr_str]
    target = int(input("目标值：\n"))
    res = solu.minSubArrayLenBisect(target, arr)
    print(res)