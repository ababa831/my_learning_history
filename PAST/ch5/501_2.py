# a1~b3は整数値であれば，Cとの条件以外は制約はなく，1通りでも組み合わせが用意できればYesになる
# したがって，Cとの条件を満たさないものをフィルタリングする考えでいく
from itertools import product
 
ab_max = [[0] * 3, [0] * 3]
cmat = []
sum_cmat = 0
for _ in range(3):
    row = list(map(int, input().split()))
    cmat.append(row)
    sum_cmat += sum(row)

if sum_cmat % 3 != 0:
    print('No')
    exit()
 
for i in range(1, 3):
    col1 = cmat[i][0] - cmat[i-1][0]
    col2 = cmat[i][1] - cmat[i-1][1]
    col3 = cmat[i][2] - cmat[i-1][2]
    if not (col1 == col2 and col2 == col3):
        print('No')
        exit()
for j in range(1, 3):
    row1 = cmat[0][j] - cmat[0][j-1]
    row2 = cmat[1][j] - cmat[1][j-1]
    row3 = cmat[2][j] - cmat[2][j-1]
    if not (row1 == row2 and row2 == row3):
        print('No')
        exit()

print('Yes')