# Code By : Sam._.072

# Time complexity : O(n)
# Space complexity : O(n)
# Logic : at each index we have to check its left heighest and its right heighest and 
# apply min(left heighest , right heighest) - current height
 

def trap(a):
    n = len(a)
    l = [0 for i in range(n)]
    r = [0 for i in range(n)]
    h = a[0]
    for i in range(n):
        if a[i] > h:
            h = a[i]
        l[i] = h
    h = a[-1]
    for i in range(n-1,-1,-1):
        if a[i] > h:
            h = a[i]
        r[i] = h
    c = 0
    for i in range(n):
        c += min(l[i], r[i])-a[i]
    return c


if __name__=='__main__':
    a=list(map(int,input().split()))
    print(trap(a))