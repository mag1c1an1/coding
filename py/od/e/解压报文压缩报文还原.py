compressed = input()
stk = [["", 1, ""]]
curr_str = ""
curr_num = ""

for c in compressed:
    if c.isalpha():
        curr_str += c
    elif c.isdigit():
        curr_num += c
    elif c == "[":
        stk.append([curr_str, int(curr_num), ""])
        curr_str = curr_num = ""
    else:
        prev_str, time, prev_res = stk.pop()
        stk[-1][-1] += prev_str + time * (prev_res + curr_str)
        curr_str = ''

res = stk.pop()[-1] + curr_str
print(res)