# a) [24]
# b) ZZZZZ [2]
# c) 104 [104]
# d) 3600 [0] x 4394 (missed out R in the alphabet)
s = list(input())
for i in range(len(s)-1, 0, -1):
    s[i] = chr((ord(s[i])-ord(s[i-1])-ord('A')*2-1)%26+ord('A'))
print(''.join(s))

# d)
# def encrypt(s):
#     s = list(s)
#     for i in range(1, len(s)):
#         s[i] = chr((ord(s[i-1])+ord(s[i])-ord('A')*2+1)%26+ord('A'))
#     return(''.join(s))
# c = 0
# alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# for i in alpha:
#     for j in alpha:
#         for k in alpha:
#             s = i+j+k
#             orig = i+j+k
#             for _ in range(52-39):
#                 s = encrypt(s)
#             if s == orig:
#                 c += 1
# print(c)