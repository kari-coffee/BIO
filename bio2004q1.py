date = [int(i) for i in input().split()]
initial = [13, 20, 7, 16, 3]

for i in range(5):
    date[i] -= initial[i]
b, k, t, u, kins = [i for i in date]
k += b*20
t += k*20
u += t*18
kins += u*20

year = kins // 365
kins -= 365*year

year += 2000 # account for initial year
kins -= sum([1 if i % 4 == 0 else 0 for i in range(2001, year)])

months = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
if year % 4 == 0: # leap year
    months[2] = 29

month = 1
for i in range(1, 13):
    if kins > months[i]:
        month += 1
        kins -= months[i]
    else:
        break
print(kins, month, year)
