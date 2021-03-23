from itertools import combinations
import copy

S = input()
S_len = len(S)
T_maxlen = min(3, S_len)

canditates = []
for case_tlen in range(1, T_maxlen+1):
    for curr, _ in enumerate(S):
        if curr + case_tlen > S_len:
            break
        selected = S[curr:curr+case_tlen]
        # e.g. T ∈ {'ab', 'a.', '.b', '..'}
        canditates.append(selected)  # pattern: 'ab'
        for i in range(1, case_tlen+1):
            # search index of '.' insertion
            insert_idx_list = list(combinations(range(case_tlen), i))
            for idx_tup in insert_idx_list:
                inserted = list(copy.copy(selected))
                for idx in idx_tup:
                    inserted[idx] = '.'
                canditates.append(''.join(inserted))

patterns = set(canditates)
print(len(patterns))

