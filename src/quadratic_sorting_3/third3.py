first_in = input().split(' ')
second_in = input().split(' ')

n = int(first_in[0])
k = int(first_in[1])

volumes = [int(v) for v in second_in]

for i in range(k):
    imax = i
    for j in range(i + 1, n):
        if volumes[j] > volumes[imax]:
            imax = j
    volumes[i], volumes[imax] = volumes[imax], volumes[i]

print(volumes[k-1])
