class Solution:
    def isAlienSorted(self, words, order) -> bool:
        for i in range(1, len(words)):
            latter = words[i]
            former = words[i-1]
            j = 0
            while j<len(latter) and j <len(former) and latter[j] == former[j]:
                j += 1
            diff_former = order.index(former[j]) if j < len(former) else None
            diff_latter = order.index(latter[j]) if j < len(latter) else None
            if diff_former is not None and diff_latter is not None:
                if diff_former > diff_latter:
                    return False
                else:
                    continue
            elif diff_former is not None and diff_latter is None:
                return False

        return True


if __name__ == '__main__':
    solu = Solution()
    words = input("words：\n").split()
    order = input("order:\n")
    res = solu.isAlienSorted(words, order)
    print(res)