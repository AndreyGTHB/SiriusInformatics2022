def scan(a,n,b,m):
    ishirt=0
    ipant=0
    imin=abs(a[0]-b[0])
    mshirt=0
    mpant=0
    while (True):
        if (ishirt >= n) | (ipant >=m):
            break
        if a[ishirt]==b[ipant]:
            mshirt=ishirt
            mpant=ipant
            break
        if abs(a[ishirt]-b[ipant]) < imin:
            imin=abs(a[ishirt]-b[ipant])
            mshirt=ishirt
            mpant=ipant
        if (a[ishirt] < b[ipant]):
            ishirt+=1
        else:
            ipant+=1
    print(str(a[mshirt])+" "+str(b[mpant]))


n = int(input())
shirts = list(map(int, input().split()))
m = int(input())
pants = list(map(int, input().split()))

scan(shirts, n, pants, m)
