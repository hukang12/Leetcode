class NumMatrix:

    def __init__(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        pre_region = [[0 for _ in range(cols + 1)] for _ in range(rows + 1)]
        for row in range(1, rows + 1):
            for col in range(1, cols + 1):
                pre_sum = pre_region[row - 1][col] + pre_region[row][col - 1] - pre_region[row - 1][col - 1] + \
                          matrix[row - 1][col - 1]
                pre_region[row][col] = pre_sum
        self.pre_region = pre_region

    # 暴力——超时
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum = 0
        for row in range(row1, row2+1):
            for col in range(col1, col2+1):
                sum += self.matrix[row][col]
        return sum

    # 前缀和
    def sumRegion2(self, row1: int, col1: int, row2: int, col2: int) -> int:
        pre_region = self.pre_region
        up = pre_region[row1][col2+1]
        left = pre_region[row2+1][col1]
        left_up = pre_region[row1][col1]
        cur = pre_region[row2+1][col2+1]
        sum = cur-left-up+left_up
        return sum

if __name__ == '__main__':
    a = [
        [3,0,1,4,2],
        [5,6,3,2,1],
        [1,2,0,1,5],
        [4,1,0,1,7],
        [1,0,3,0,5]
    ]
    nm = NumMatrix(a)
    do = [
        [2,1,4,3],
        [1,1,2,2],
        [1,2,2,4]
    ]
    res = []
    for (a,b,c,d) in do:
        r = nm.sumRegion2(a,b,c,d)
        res.append(r)
    print(res)
