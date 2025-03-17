import sys

# 给定一行文本，识别其是否符合数组格式（数组可嵌套）。例如，下列每行文本均符合数组格式:[]
# [v1,v2,v3]
# [v1,v2,[],v3]
# [v1,v2,[v3,v4],v5]
# [v1,v2,[v3,[v4]],v5]
# 具体而言，数组格式要求包括:
# 数组一定以左中括号"["开头、以右中括号"]"结尾。数组可包含任意数目的数组元素(可以为0个)，元素之间以逗号","分隔
# 数组元素可以是文本，也可以是嵌套数组。其中，数组元素如果是文本，则包含至少一个字符，并且不包含特殊字符“[”、"]”;数组元素如果是嵌套数组，则嵌套数组也符合格式要求。
# 而对于不符合数组格式的文本，请你计算其“合法前缀"的长度，以便提示改正。"合法前缀"是指:截至这个前缀处都符合数组格式，即存在某一行文本具有这一前缀。


def solve(line):
    line = line.strip()
    prev = None
    if prev is None and line[0] != "[":
        print("invalid 0")
        return
    s = 0
    i = 0
    while i < len(line):
        c = line[i]
        if c == ",":
            if prev == "," or prev == "[" or s <= 0:
                print(f"invalid {i}")
                return
            prev = ","
        elif c == "[":
            if prev is not None and prev != ",":
                # prev is invalid
                print(f"invalid {i}")
                return
            prev = "["
            s += 1
        elif c == "]":
            s -= 1
            if prev == "," or s < 0:
                print(f"invalid {i}")
                return
            prev = "]"
        else:
            j = i
            while (
                j < len(line) and line[j] != "," and line[j] != "[" and line[j] != "]"
            ):
                j += 1
            cur = line[i:j]
            if prev != "[" and prev != ",":
                print(f"invalid {i}")
                return
            if s <= 0:
                print(f"invalid {i}")
                return
            i = j - 1
            prev = cur
        i += 1
    if s == 0:
        print(f"valid")
    else:
        print(f"invalid {len(line)}")


for line in sys.stdin:
    solve(line)
