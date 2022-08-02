#与えられたリストの累積和のリストを返すよ
def Cum_Sum(l):
  ret=[0]*len(l)
  ret[0]=l[0]
  for i in range(1,len(l)):
    ret[i]=l[i]+ret[i-1]
  return ret
