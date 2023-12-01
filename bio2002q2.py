s = input()
deck = [i for i in range(1, 9)]
def b(deck):
    return deck[1:] + [deck[0]]
def riffle(deck, x):
    res = []
    half = len(deck)//2
    for i in range(0, half):
        if x == 'o':
            res.append(deck[i])
            res.append(deck[i+half])
        else:
            res.append(deck[i+half])
            res.append(deck[i])
    return res

def shuffle(deck, s):
    if s == "":
        return deck
    new = s[1:]
    if s[0] == 'b':
        deck = b(deck)
    elif s[0] == 'i':
        deck = riffle(deck, 'i')
    elif s[0] == 'o':
        deck = riffle(deck, 'o')
    else: #s[0] is a number
        start_ix, end_ix = 1, 2
        if s[1] == '(':
            start_ix = 2
            count = 0
            for j in range(2, len(s)):
                if s[j] == '(':
                    count += 1
                if s[j] == ')':
                    if count == 0:
                        end_ix = j
                        break
                    count -= 1
        for _ in range(int(s[0])):
            deck = shuffle(deck, s[start_ix:end_ix])
        new = s[end_ix+1:]
    deck = shuffle(deck, new)
    return deck
    
deck = shuffle(deck, s)
print(*deck)

#b)
# deck = [i for i in range(1, 21)]
# deck = shuffle(deck, 'bio')
# print(*deck)

#c)
#in riffles:
# deck = [i for i in range(1, 9)]
# count = 0
# while True:
#     deck = b(deck)
#     count += 1

#d)
# deck = [i for i in range(1, 7)]
# count = 0
# while True:
#     deck = riffle(deck, 'i')
#     count += 1