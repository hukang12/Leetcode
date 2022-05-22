# -- coding: utf-8 --
# @Time : 2022/5/21 22:33
# @Author : HK
# @File : 040.py
from collections import deque

class Solution:
    # 单调栈
    def largestRectangleArea(self, heights: [int]) -> int:
        stack = deque([-1])
        heights.append(0)
        max_rec_area = 0
        for i,h in enumerate(heights):
            while stack and stack[-1] != -1 and h < heights[stack[-1]]:
                mid_id = stack.pop()
                left_id = stack[-1]
                tmp_area = heights[mid_id] * (i-left_id-1)
                if tmp_area > max_rec_area: max_rec_area = tmp_area
            stack.append(i)

        return max_rec_area

    # histogram
    def maximalRectangle(self, matrix) -> int:
        if not matrix: return 0
        max_area = 0
        dim2len = len(matrix[0])
        heights = [0] * dim2len
        for str in matrix:
            for i in range(len(str)):
                a = int(str[i])
                heights[i] = heights[i]+a if a else 0
            tmp_area = self.largestRectangleArea(heights)
            if tmp_area>max_area: max_area = tmp_area
        return max_area

if __name__ == '__main__':
    matrix = ["10100","10111","11111","10010"]
    matrix = []
    matrix = ["10"]
    # str = input("数组:\n").split()
    # arr = [int(a) for a in str]
    s = Solution()
    res = s.maximalRectangle(matrix)
    print(res)