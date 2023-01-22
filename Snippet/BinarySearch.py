ok=n#OKであることが保証されている値
ng=-1#NGであることが保証されている値
while abs(ok-ng)>1:
    mid=(ok+ng)//2
    if solve(mid):ok=mid #solve関数は判定する関数
    else:ng=mid
