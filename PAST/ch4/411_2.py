# sortedを使わず自力で実装できるようにしろ
abcdef = list(map(int, input().split()))
abcdef = sorted(abcdef, reverse=True)

print(abcdef[2])