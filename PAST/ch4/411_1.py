S = input().split()

n_a = S.count('a')
n_b = S.count('b')
n_c = S.count('c')

n_max = max(n_a, n_b, n_c)

if n_a == n_max:
    print('a')
elif n_b == n_max:
    print('b')
else:
    print('c')