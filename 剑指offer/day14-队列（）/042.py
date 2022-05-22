# -- coding: utf-8 --
# @Time : 2022/5/22 16:43
# @Author : HK
# @File : 042.py
from collections import deque
class RecentCounter:

    def __init__(self):
        self.queue = deque([])

    def ping(self, t: int) -> int:
        if not self.queue:
            self.queue.append(t)
        else:
            while self.queue and self.queue[0] < (t-3000):
                self.queue.popleft()
            self.queue.append(t)
        return len(self.queue)



if __name__ == '__main__':
    # Your RecentCounter object will be instantiated and called as such:
    inputs = ["RecentCounter", "ping", "ping", "ping", "ping"]
    inputs = [[], [1], [100], [3001], [3002]]

    obj = RecentCounter()
    param_1 = obj.ping(1)
    param_2 = obj.ping(100)
    param_3 = obj.ping(3000)
    param_3 = obj.ping(3001)
    param_4 = obj.ping(3002)
    print(param_1,param_2,param_3,param_4)