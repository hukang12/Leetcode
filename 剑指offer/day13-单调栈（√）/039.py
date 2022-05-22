#!/usr/bin/env Python
# coding=utf-8
# @Time : 2022/5/21 11:43
# @Author : HK
# @File : 039.py
from collections import deque

class Solution:
    # 暴力-超时
    def largestRectangleArea2(self, heights: [int]) -> int:
        h_len = len(heights)
        max_rec_area = 0
        for i in range(h_len):
            cur_h = heights[i]
            left, right = i-1, i+1
            while left >= 0 and heights[left] >= cur_h:
                left -= 1
            while right < h_len and heights[right] >= cur_h:
                right += 1
            rec_area = (right-left-1)*cur_h
            if rec_area > max_rec_area:
                max_rec_area = rec_area
        return max_rec_area

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

if __name__ == '__main__':
    # str = input("数组:\n").split(",")
    str = input("数组:\n").split()
    arr = [int(a) for a in str]
    s = Solution()
    res = s.largestRectangleArea(arr)
    print(res)