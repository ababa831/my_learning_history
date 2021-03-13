# B - A < 1000 より，全探索で時間制限に間に合う
K = int(input())
A, B = map(int, input().split())

for i in range(A, B+1):
    if i % K == 0:
        print('OK')
        exit()
print('NG')