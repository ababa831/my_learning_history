# O(N^2)
N = int(input())
smat = [list(input()) for _ in range(N)]

for i in reversed(range(N - 1)):
    for j in range(1, 2 * N - 2):
        cond1 = smat[i + 1][j - 1] == 'X'
        cond2 = smat[i + 1][j] == 'X'
        cond3 = smat[i + 1][j + 1] == 'X'
        cond4 = smat[i][j] == '#'

        if cond4 and (cond1 or cond2 or cond3):
            smat[i][j] = 'X'

for row in smat:
    print(''.join(row))
