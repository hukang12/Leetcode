# -- coding: utf-8 --
# @Time : 2022/5/22 16:34
# @Author : HK
# @File : 041.py
from collections import deque
class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.queue = deque([])
        self.window = size
        self.sum = 0


    def next(self, val: int) -> float:
        cur_len = len(self.queue)
        if cur_len < self.window:
            self.queue.append(val)
            self.sum += val
            return self.sum/(cur_len+1)
        tmp = self.queue.popleft()
        self.sum -= tmp
        self.queue.append(val)
        self.sum += val
        return self.sum/cur_len


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
if __name__ == '__main__':
    inputs = ["MovingAverage", "next", "next", "next", "next"]
    inputs = [[3], [1], [10], [3], [5]]
