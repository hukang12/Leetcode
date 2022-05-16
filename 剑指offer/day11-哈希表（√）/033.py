from collections import Counter

class Solution:
    def groupAnagrams(self, strs):
        # if len(strs) == 1: return [strs]
        res = []
        count = 0
        cur_dict = {}
        for str in strs:
            sorted_str = ''.join(sorted(str))
            if sorted_str in cur_dict:
                res[cur_dict[sorted_str]].append(str)
            else:
                cur_dict[sorted_str] = count
                count += 1
                res.append([str])
        return res

    # 暴力破解，超时
    def groupAnagrams2(self, strs):
        res = []
        cur_dict_list = []
        for str in strs:
            str_dict = Counter(str)
            i=0
            while i < len(cur_dict_list):
                di = cur_dict_list[i]
                if str_dict == di:
                    res[i].append(str)
                    break
                i += 1
            if i == len(cur_dict_list):
                cur_dict_list.append(str_dict)
                res.append([str])
        return res


if __name__ == '__main__':
    solu = Solution()
    words = input("words：\n").split()
    res = solu.groupAnagrams(words)
    print(res)