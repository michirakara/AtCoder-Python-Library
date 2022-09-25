#nの約数を昇順に列挙するよ
#https://qiita.com/LorseKudos/items/9eb560494862c8b4eb56を参考にしました
def make_divisors(n):
    lo,up=[],[]
    i=1
    while i*i<=n:
        if n%i==0:
            lo.append(i)
            if i!=n//i:
                up.append(n//i)
        i+=1
    return lo+up[::-1]
