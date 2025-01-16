"""
存在一种虚拟IPv4地址，由4小节组成，每节的范围为0~255，以#号间隔，虚拟IPv4地址可以转换为一个32位的整数，例如：

128#0#255#255，转换为32位整数的结果为2147549183（0x8000FFFF）

1#0#0#0，转换为32位整数的结果为16777216（0x01000000）

现以字符串形式给出一个虚拟IPv4地址，限制第1小节的范围为1128，即每一节范围分别为(1128)#(0255)#(0255)#(0~255)，要求每个IPv4地址只能对应到唯一的整数上。如果是非法IPv4，返回invalid IP

输入描述
输入一行，虚拟IPv4地址格式字符串

输出描述
输出一行，按照要求输出整型或者特定字符

示例1
输入

100#101#1#5
1
输出

1684340997
1
说明

示例2
输入

1#2#3
1
输出

invalid IP
1
说明
"""
ip = input()

ip_sec = list(ip.split('#'))


nums = []

def is_valid(ip_sec):
    if len(ip_sec) != 4:
        return False
    
    for i in range(4):
        n  = 0
        if not ip_sec[i].isdigit():
            return False
        n = int(ip_sec[i])
        if i == 0:
            if n < 0 or n > 128:
                return False
        else:
            if n < 0 or n > 255:
                return False
        nums.append(n)
    return True

def solve(ip_sec):
    if not is_valid(ip_sec):
        print("Invalid IP")
        return
    out = 0
    print(nums)
    for i,n in enumerate(nums):
        out |= n << ((3-i) * 8)
    
    print(out)

solve(ip_sec)