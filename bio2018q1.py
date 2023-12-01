# a) [26]
# b) 5 [2]
# c) 100 100 x 96 49
from math import ceil
debt = 10000
i, r = [int(i) for i in input().split()]
repaid = 0
while debt > 0:
    increase = debt*i/100
    debt = ceil(debt+increase)
    repay = ceil(debt * r/100)
    if repay < 5000:
        repay = 5000
    if debt-repay < 0:
        repaid += debt/100
        debt = 0
    else:
        debt -= repay
        repaid += repay/100
print(round(repaid, 2))

# part c
# ans = 0
# a, b = 0, 0
# for i in range(101):
#     for r in range(1, 101):
#         valid = True
#         debt = 10000
#         repaid = 0
#         while debt > 0:
#             increase = debt*i/100
#             debt = ceil(debt+increase)
#             repay = ceil(debt * r/100)
#             if repay < 5000:
#                 repay = 5000
#             if debt-repay < 0:
#                 repaid += debt/100
#                 debt = 0
#             else:
#                 debt -= repay
#                 repaid += repay/100
#             if debt >= 10000:
#                 valid = False
#                 break
#         if repaid > ans and valid:
#             ans = repaid
#             a = i
#             b = r

# print(ans)
# print(a, b)