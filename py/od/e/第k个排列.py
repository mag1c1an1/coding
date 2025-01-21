# """
# class Solution:
#     def getPermutation(self, n: int, k: int) -> str:
#         from math import factorial
#         res = ""
#         nums = [i for i in range(1,n+1)]
#         n,k = len(nums),k-1
#         while n > 0:
#             cur = factorial(n-1)
#             idx,k = divmod(k,cur)
#             res += str(nums.pop(idx))
#             n -= 1
#         return res


# class Solution:
#     def getPermutation(self, n: int, k: int) -> str:
#         factorial = [1]
#         for i in range(1, n):
#             factorial.append(factorial[-1] * i)

#         k -= 1
#         ans = list()
#         valid = [1] * (n + 1)
#         for i in range(1, n + 1):
#             order = k // factorial[n - i] + 1
#             for j in range(1, n + 1):
#                 order -= valid[j]
#                 if order == 0:
#                     ans.append(str(j))
#                     valid[j] = 0
#                     break
#             k %= factorial[n - i]

#         return "".join(ans)

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/permutation-sequence/solutions/401574/di-kge-pai-lie-by-leetcode-solution/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
# """
# n = int(input())
# k = int(input())


# if n == 1:
#     print("1")
#     exit()

# nums = [i + 1 for i in range(n)]
# result = []


# def generatePermutations(nums, current, result, k):
#     if len(nums) == 0:
#         result.append(current)
#         return

#     for i in range(len(nums)):
#         num = nums[i]
#         newNums = nums[:i] + nums[i + 1 :]
#         generatePermutations(newNums, current + str(num), result, k)

#         if len(result) == k:
#             return


# generatePermutations(nums, "", result, k)

# result.sort()
# print(result[k - 1])


# # def generate_permutations(elements):
# #     def backtrack(start):
# #         # 如果到达最后一个元素，将当前排列加入结果
# #         if start == len(elements):
# #             result.append(elements[:])
# #             return

# #         # 遍历每个可能的选项
# #         for i in range(start, len(elements)):
# #             # 交换元素
# #             elements[start], elements[i] = elements[i], elements[start]
# #             # 递归生成下一个位置的排列
# #             backtrack(start + 1)
# #             # 撤销交换（回溯）
# #             elements[start], elements[i] = elements[i], elements[start]

# #     result = []
# #     backtrack(0)
# #     return result


# # # 测试
# # elements = [1, 2, 3]
# # result = generate_permutations(elements)
# # print("全排列结果：")
# # for perm in result:
# #     print(perm)


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        from math import factorial

        res = ""
        nums = [i for i in range(1, n + 1)]
        n, k = len(nums), k - 1
        while n > 0:
            cur = factorial(n - 1)
            idx, k = divmod(k, cur)
            res += str(nums.pop(idx))
            n -= 1
        return res


res = Solution().getPermutation(3, 3)

print(res)
