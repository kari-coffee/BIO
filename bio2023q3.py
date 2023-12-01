# a) [23]
# b) 288 [2]
# c) 192, 3072? x 73, 375
# d) 1,1,1,1,1,7,17,17 x 1,1,2,3,3,3,8,8

start = input().split()
end = input().split()
for i in range(4):
    if start[i] == '0':
        start[i] = ''
    if end[i] == '0':
        end[i] = ''

done = set()
done.add(tuple(start))
queue = [[start, 0]]
ans = -1
while queue:
    state, moves = queue.pop(0)
    if state == end:
        if moves < ans or ans == -1:
            ans = moves
    else:
        done.add(tuple(state))
        for i in range(4):
            for j in range(4):
                if state[i] != '' and i != j:
                    piece = state[i][-1]
                    new = state[:i]+[state[i][:-1]]+state[i+1:]
                    new[j] += piece
                    if tuple(new) not in done:
                        queue.append([new, moves+1])
                        
print(ans)
