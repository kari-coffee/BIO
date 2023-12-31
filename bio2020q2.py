# a) [24]
# b) A, AAAA [2]
# c) The spy can count the number of times they have exited the room, 
# which will be equivalent to the number of times they have visited it - 1
# This allows them to continue with their route based on whether it is an odd or even number
# d) Done below

# from collections import defaultdict
# plan, p, q = input().split()
# p, q = int(p), int(q)
# alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'[:len(plan)+2]

# complex = defaultdict(lambda: [])
# chosen = set()
# while plan:
#     for letter in alpha:
#         if letter not in plan and letter not in chosen:
#             complex[letter].append(plan[0])
#             complex[plan[0]].append(letter)
#             chosen.add(letter)
#             plan = plan[1:]
#             break
# unused = [i for i in alpha if i not in chosen]
# complex[unused[0]].append(unused[1])
# complex[unused[1]].append(unused[0])
# for i in alpha:
#     complex[i] = sorted(complex[i])
#     print(''.join(complex[i]))

# cur = 'A'
# visited =  {i:0 for i in alpha}
# left = {k:[0 for i in range(len(complex[k]))] for k, v in complex.items()}
# ans = ''
# for i in range(q):
#     visited[cur] += 1
#     if i == p:
#         print(cur, end='')
#     if visited[cur] % 2 != 0:
#         left[cur][0] += 1
#         cur = complex[cur][0]
#     else:
#         for j in range(len(complex[cur])):
#             if left[cur][j] % 2 != 0:
#                 if j == len(complex[cur])-1:
#                     left[cur][j] += 1
#                     cur = complex[cur][j]
#                     break
#                 left[cur][j+1] += 1
#                 cur = complex[cur][j+1]
#                 break
# print(cur)

# c) answer given by ms is 96 but I'm fairly sure it is 54 (cross checked with another solution)
# from itertools import product
# from collections import defaultdict
# alpha = 'ABCDEFGH'
# ans = 0
# for plan in product(alpha, repeat=6):
#     plan = ''.join(plan)
#     complex = defaultdict(lambda: [])
#     chosen = set()
#     c = 0
#     while plan:
#         for letter in alpha:
#             if letter not in plan and letter not in chosen:
#                 complex[letter].append(plan[0])
#                 complex[plan[0]].append(letter)
#                 chosen.add(letter)
#                 plan = plan[1:]
#                 c += 1
#                 break
#         if c == 4:
#             break
#     if complex['A'] == ['E'] and complex['B'] == ['F'] and complex['C'] == ['G'] and complex['D'] == ['H']:
#         ans += 1
# print(ans)
    
    