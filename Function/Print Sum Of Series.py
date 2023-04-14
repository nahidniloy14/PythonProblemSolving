def sum_series(n,a,r):
    s=0
    for i in range(1,n+1):
        s+=a*(r**(i-1))

    return s
first_term=a=2
ratio=r=3
series=n=5

print(sum_series(n,a,r))