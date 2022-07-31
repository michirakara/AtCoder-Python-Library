#col行ある二次元配列を受け取るよ
def l_int_two_dim_in(col):
  return [[*map(int,input().split())] for i in range(col)]
