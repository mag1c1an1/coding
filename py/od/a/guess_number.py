# 输入获取
# n = int(input())
# infos = [input().split() for _ in range(n)]


# 获取猜的数字guess在指定谜底answer下的猜测提示
def getGuessResult(guess, answer):
    countA = 0
    countB = 0

    # 判断不同
    answer_arr = [0] * 10
    guess_arr = [0] * 10

    for i in range(len(guess)):
        c1 = int(guess[i])
        c2 = int(answer[i])

        if c1 == c2:
            countA += 1
        else:
            guess_arr[c1] += 1
            answer_arr[c2] += 1

    for i in range(10):
        # 最小值才是要统计的
        countB += min(answer_arr[i], guess_arr[i])

    return f"{countA}A{countB}B"


# 判断谜底answer是否正确，即是否符合所有猜测提示
def isValid(answer):
    for info in infos:
        guess, expect_result = info
        real_result = getGuessResult(guess, answer)
        if expect_result != real_result:
            return False
    return True


# 剪枝逻辑，本题的后期优化主要在这个方法内进行
# 返回的是一个列表，列表有四个元素，分别对应四码的谜底数字的每一位，而每个列表元素又是一个列表，里面存放谜底数字对应的位上可能是哪些数字
def getCombine():
    # 初始时，四码谜底的每一位都有十种可能，即每一位都能取值0~9
    num = [set([i for i in range(10)]) for _ in range(4)]

    # 遍历猜谜者猜的数字guess_num与提示guess_result
    for info in infos:
        guess_num, guess_result = info

        # 数字正确且位置正确的个数
        countA = int(guess_result[0])
        # 数字正确而位置不对的数的个数
        countB = int(guess_result[2])

        # 如果countA == 0,则说明当前guess_num的每一位上的数字的位置都不正确，即对应位上不应该出现对应数字
        if countA == 0:
            for i in range(4):
                c = int(guess_num[i])
                if countB == 0:
                    # 如果countB == 0，则说明当前guess_num上所有位上的数字都不正确，即任意位上都不应该出现该数字
                    num[0].discard(c)
                    num[1].discard(c)
                    num[2].discard(c)
                    num[3].discard(c)
                else:
                    num[i].discard(c)

    return num


# 算法入口
def getResult():
    num = getCombine()
    cache = []

    for c1 in num[0]:
        for c2 in num[1]:
            for c3 in num[2]:
                for c4 in num[3]:
                    answer = f"{c1}{c2}{c3}{c4}"
                    if isValid(answer):
                        cache.append(answer)

    # 答案不确定则输出NA
    if len(cache) != 1:
        return "NA"
    else:
        return cache[0]


def my_count_diff(num1,nums2):
    s1 = str(num1)
    s2 = str(num2)
    
    cnt1 = [0] * 10
    cnt2 = [0] * 10


    for i in range(len(s1)):
        c1 = int(s1[i])
        c2 = int(s2[i])

        if c1 != c2:
            cnt1[c1] += 1
            cnt2[c2] += 1
    
    ans = 0
    for i in range(10):
        ans += min(cnt1[i],cnt2[i])
    return ans
            



def count_different_positions(num1, num2):

    # 将数字转为字符串
    str1 = str(num1)
    str2 = str(num2)
    
    # 初始化计数器
    count = 0
    
    # 创建数字频率字典
    freq1 = {}
    freq2 = {}
    
    # 记录每个数字的出现频率
    for digit in str1:
        if digit in freq1:
            freq1[digit] += 1
        else:
            freq1[digit] = 1
            
    for digit in str2:
        if digit in freq2:
            freq2[digit] += 1
        else:
            freq2[digit] = 1
            
    # 计算相同数字但位置不同的数量
    for digit in freq1:
        if digit in freq2:
            count += min(freq1[digit], freq2[digit])
    
    # 计算相同数字在同一位置的数量
    same_position = sum(1 for i in range(4) if str1[i] == str2[i])
    
    # 返回相同数字但位置不同的数量
    return count - same_position

# 示例
num1 = 1234
num2 = 2413
result = my_count_diff(num1, num2)
print(result)  # 输出 4，因为 1, 2, 3, 4 都相同，但位置不同



# 算法调用
# print(getResult())
