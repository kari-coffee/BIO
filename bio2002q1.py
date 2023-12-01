d = {'pa':1,'re':2,'ci':3,'vo':4,'mu':5,'xa':6,'ze':7,'bi':8,'so':9,'no':0}
s = input()
res = ''
for i in range(0, len(s), 2):
    res += str(d[s[i]+s[i+1]])
print(res)

# 2nd time solving problem
d = {0:'no', 1:'pa', 2:'re', 3:'ci', 4:'vo', 5:'mu', 6:'xa', 7:'ze', 8:'bi', 9:'so'}
d2 = {v:k for k, v in d.items()}
s = input()
s = [s[i]+s[i+1] for i in range(0, len(s)-1, 2)]
print(''.join(str(d2[i]) for i in s))