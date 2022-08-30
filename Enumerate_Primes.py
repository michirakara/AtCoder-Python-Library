#エラトステネスの篩を使ってnまでの数がそれぞれ素数かどうか判定した配列を返すよ
def enum_prime(n):
  is_prime=[1]*(n+1)
  is_prime[0],is_prime[1]=0,0
  sqrt=int(n**(0.5)+1)
  for i in range(2,sqrt):
    if is_prime[i]:
      for j in range(2*i,n+1,i):
        is_prime[j]=0
  return is_prime
