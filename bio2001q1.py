# q1 a)
n = [i+1 for i in range(int(input()))]
w = int(input())
i = -1
while len(n) > 1:
    i += w
    i %= len(n)
    n.pop(i)
    i -= 1
print(n[0])

# c) 1 also works???
# n = [i+1 for i in range(100)]
# def solve(w):
#     i = -1
#     n1 = [i for i in n]
#     while len(n1) > 1:
#         i += w
#         i %= len(n1)
#         n1.pop(i)
#         i -= 1
#     left = n1[0]
#     i = 1
#     n2 = [i for i in n]
#     while len(n2) > 1:
#         i -= w
#         while i < -len(n2):
#             i += len(n2)
#         n2.pop(i)
#         i += 1
#     if n2[0] == left:
#         return True
#     else:
#         return False
# w = 2
# while True:
#     valid = solve(w)
#     if valid:
#         break
#     w += 1

# print(w)