class Solution:
    def findMinDifference(self, timePoints) -> int:
        time2num = []
        for t in timePoints:
            ti = [int(i) for i in t.split(":")]
            time2num.append(ti[0]*60+ti[1])

        # 排序
        time2num.sort()
        min_diff = 1440
        for i in range(1, len(time2num)):
            diff = time2num[i]-time2num[i-1]
            if diff < min_diff: min_diff = diff

        final_diff = time2num[0]+1440-time2num[-1]
        if final_diff < min_diff: min_diff = final_diff
        return min_diff


if __name__ == '__main__':
    solu = Solution()
    times = input("时间：\n").split()
    res = solu.findMinDifference(times)
    print(res)