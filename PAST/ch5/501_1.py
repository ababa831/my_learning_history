# Ref: https://atcoder.jp/contests/abc157/tasks/abc157_b
Amat = [list(map(int, input().split())) for _ in range(3)]
N = int(input())
bbb = [int(input()) for _ in range(N)]

flag = False
for i, v in enumerate(bbb):
    for r_j, row in enumerate(Amat):
        try:
            col_idx = row.index(v)
            Amat[r_j][col_idx] = 0 
            if i >= 2 and Amat[r_j].count(0) == 3:
                print('Yes')
                exit()
            break
        except ValueError:
            pass
    if i >= 2:
        for col_idx in range(3):
            if Amat[0][col_idx] + Amat[1][col_idx] + Amat[2][col_idx] == 0:
                print('Yes')
                exit()
        if Amat[0][0] + Amat[1][1] + Amat[2][2] == 0 or Amat[0][2] + Amat[1][1] + Amat[2][0] == 0:
            print('Yes')
            exit()            

print('No')

