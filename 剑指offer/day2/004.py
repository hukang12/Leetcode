class Solution:
    def singleNumber(self, nums) -> int:
        one = []
        three = []
        for num in nums:
            if num in three:
                continue
            if num in one:
                three.append(num)
                one.remove(num)
            else:
                one.append(num)
        assert len(one) == 1
        return one[0]


if __name__ == '__main__':
    s = Solution()
    arr = input("输入数组：\n").split(",")
    a = [int(i) for i in arr]
    res = s.singleNumber(a)
    print(res)