class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity  # 缓存容量
        self.cache_d = [tuple()] * capacity  # 缓存器
        self.opera_sta = [-1] * capacity  # 缓存器各位置最近使用的时间，-1代表未使用过
        self.opera_id = 0  # 操作的序号

    def get(self, key: int) -> int:
        latest_id = -1
        res_v = None
        for i in range(self.capacity):
            if not self.cache_d[i]:
                return -1
            (k, v) = self.cache_d[i]
            if k == key:
                if self.opera_sta[i] > latest_id:
                    latest_id = i
                    res_v = v

        if res_v is not None:
            self.opera_sta[latest_id] = self.opera_id
            self.opera_id += 1
            return res_v
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        cache_len = self.capacity
        for i in range(self.capacity):
            if self.cache_d[i]:
                (k, v) = self.cache_d[i]
                if k == key:
                    self.cache_d[i] = (key, value)
        if self.opera_id < cache_len:
            for i in range(cache_len):
                if self.opera_sta[i] < 0:
                    self.opera_sta[i] = self.opera_id
                    self.opera_id += 1
                    self.cache_d[i] = (key, value)
                    break
        else:
            # 缓存满了，找最近未使用的位置i
            target_id = self.opera_id
            target_pos = -1
            for i, op_id in enumerate(self.opera_sta):
                if op_id < target_id:
                    target_id = op_id
                    target_pos = i
            self.opera_sta[target_pos] = self.opera_id
            self.opera_id += 1
            self.cache_d[target_pos] = (key, value)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
if __name__ == '__main__':
    # op_list = ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
    # in_list = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]

    # op_list = ["LRUCache", "get"]
    # in_list = [[1], [0]]

    # op_list = ["LRUCache", "put", "put", "get", "put", "put", "get"]
    # in_list = [[2], [2, 1], [2, 2], [2], [1, 1], [4, 1], [2]]

    op_list = ["LRUCache", "get", "put", "get", "put", "put", "get", "get"]
    in_list = [[2], [2], [2, 6], [1], [1, 5], [1, 2], [1], [2]]
    my_cache = None
    res = []
    for i in range(len(op_list)):
        op = op_list[i]
        params = in_list[i]
        if op == "LRUCache":
            my_cache = LRUCache(params[0])
            res.append("null")
        elif op == "put":
            k, v = params[0], params[1]
            my_cache.put(k, v)
            res.append("null")
        else:
            value = my_cache.get(params[0])
            res.append(value)
        print(my_cache.opera_sta, my_cache.cache_d)
    print(res)
