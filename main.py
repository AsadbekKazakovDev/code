def main(a, b):
    if a==1 and b==1: return 0
    x =1
    while x<=a:
        x*=2
    x//=2
    r = x-b
    if r>=0:
        res = b * x*(x-1)//2
    else:
        res = x * x*(x-1)//2
        res += -r * (x*(x-1)//2 + x*x)
    if x==a: return res
    n = b
    m = a-x
    if n>x:
        res += x*m*x
        res += main(x, m)
        n -= x;
        if n<m:
            res+=main(m, n)
        else:
            res+=main(n,m)
 
    else:
        res += x*n*m;
        if n<m:
            res+=main(m, n)
        else:
            res+=main(n,m)
 
    return res;
n, m = map(int, input().split())
if n<m:
  print(main(m+1, n+1))
else:
  print(main(n+1, m+1))