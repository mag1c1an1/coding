from collections import defaultdict
import functools

"""给一堆以空格分割的字符串，将这些字符串重新排列，在保证出现顺序的前提下字典序要尽可能的小。（如果不懂题目意思请看示例）
"""


def main():
    words = list(input().split())

    first = {}
    last = {}

    for i, s in enumerate(words):
        if s not in first:
            first[s] = i
        last[s] = i

    # 自定义排序规则
    def compare(s1, s2):
        if s1 < s2:
            if first[s1] < first[s2]:
                return -1
            else:
                return 1
        elif s1 == s2:
            return 0
        else:
            if last[s1] > last[s2]:
                return 1
            else:
                return -1

    # 对数组进行排序
    words.sort(key=functools.cmp_to_key(compare))

    # # 去重输出
    seen = set()
    for s in words:
        if s not in seen:
            print(s, end=" ")
            seen.add(s)
    print()


if __name__ == "__main__":
    main()
