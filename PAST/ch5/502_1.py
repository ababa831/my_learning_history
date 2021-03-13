N = int(input())

k = 0
curr = 0
while True:
    if k < 10:
        curr +=1
    elif len(set(str(k))) == 1:
        curr += 1
    if curr == N+1:
        print(k)
        exit()
    k += 1