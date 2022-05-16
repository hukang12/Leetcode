class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        num_len = len(nums)
        start = 0
        end = 0
        product = int(1)
        count = 0
        toMul=0
        while end < num_len:
            product *= nums[end]
            toMul += 1
            while start <= end and product >= k:
                product /= nums[start]
                start += 1
                toMul -= 1
            count += toMul
            print("start:{},end{}".format(start, end))
            end += 1
        """    
        while i < num_len:
            while start <= end < num_len and product < k:
                product *= nums[end]
                end += 1
            if start<end and product >= k:
                sub_len = end-start-1
                if last_end >= 0:
                    overlap_len = last_end-start-1
                last_end = end
                count += sub_len*(sub_len+1)/2
                if overlap_len > 0:
                    count -= overlap_len*(overlap_len+1)/2
                while start <= end and product >= k:
                    product /= nums[start]
                    start += 1
            else:
                i += 1

        if product < k:
            sub_len = end-start
            if last_end >= 0:
                overlap_len = last_end-start-1
            count += sub_len*(sub_len+1)/2
            if overlap_len > 0:
                count -= overlap_len*(overlap_len+1)/2
        """
        return count


if __name__ == '__main__':
    solu = Solution()
    arr_str = input("数组：\n").split()
    arr = [int(i) for i in arr_str]
    target = int(input("目标值：\n"))
    res = solu.numSubarrayProductLessThanK(arr, target)
    print(int(res))