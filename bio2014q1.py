# a) [25]
# b) 23 [2]
# c) no answer [0] x 1_999_999_998
# (1_000_000_000) * 2 - 2 as each number generates 2 results, except the start and end numbers
odd = [i for i in range(1, 10010, 2)]
n = int(input())
cur = 0
c = 1
while c < len(odd):
    diff = odd[c]-1
    ix = odd[c]-1
    while ix < len(odd):
        if odd[ix] != 0:
            if diff+1 == odd[c]:
                odd.pop(ix)
                diff = 0
                ix -= 1
            else:
                diff += 1
        ix += 1
    c += 1

print(odd)
# low = 10001
# high = 0
# for i in odd:
#     if i < n:
#         low = i
#     elif i > n:
#         high = i
#         break
# print(low, high)

# odd = [i for i in range(1, 10010, 2)]
# n = int(input())
# cur = 0
# c = 1
# while c < len(odd):
#     diff = odd[c]-1
#     ix = odd[c]-1
#     while ix < len(odd):
#         if odd[ix] != 0:
#             if diff+1 == odd[c]:
#                 odd.pop(ix)
#                 diff = 0
#                 ix -= 1
#             else:
#                 diff += 1
#         ix += 1
#     c += 1
# print(odd)
