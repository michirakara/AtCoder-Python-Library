#str_i int_iの形の入力を受け取るよ
def ISL(n):
  l=[]*n
  for i in range(n):
    a,b=input().split()
    b=int(b)
    l[i]=[a,b]
  return l
