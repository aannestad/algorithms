def permute(seq, i, n):
    if i == n:
        retval.append(list(seq))
    for j in range(i, n):
        seq[j], seq[i] = seq[i], seq[j]
        permute(seq, i + 1, n)
        seq[j], seq[i] = seq[i], seq[j]

# Thanks Pal Drange

# retval = []
# permute(['A','B','C'],0,3)
# print(retval)