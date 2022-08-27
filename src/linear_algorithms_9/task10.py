def inc(d, key):
    if key not in d.keys():
        d[key] = 0
    d[key] += 1


def dec(d, key):
    d[key] -= 1
    if d[key] == 0:
        del d[key]


n, k = map(int, input().split())
trees = list(map(int, input().split()))


ibest = i = j = 0
jbest = n - 1
tree_dict = {trees[0]: 1}
while True:
    if len(tree_dict) < k:
        if n - j == 1:
            break
        j += 1
        inc(tree_dict, trees[j])
    else:
        if j - i < jbest - ibest:
            ibest = i
            jbest = j
        dec(tree_dict, trees[i])
        i += 1

print(ibest + 1, jbest + 1)
