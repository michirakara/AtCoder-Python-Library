#とりあえずこれをコピペしたら大丈夫だね

import sys
input=sys.stdin.readline

#一つの整数を受け取るよ
def Int():
  return int(input())

#文字列を受け取るよ(普通に入力した方がはやいね)
def Str():
  return input().rstrip()

#スペース区切りで横に並んだ整数の配列を受け取るよ
def ILH():
  return [*map(int,input().split())]

#一つの値ごとに改行されているn個の要素から成り立つ配列を受け取るよ
def ILV(n):
  return [int(input()) for i in range(n)]

#col行ある二次元配列を受け取るよ
def ILTD(col):
  return [[*map(int,input().split())] for i in range(col)]

#スペースで区切られた文字列の配列を受け取るよ
def SLH():
  return input().split()

#n行の文字列の配列を受け取るよ
def SLV(n):
  return [input().rstrip() for i in range(n)]

#str_i int_iの形の入力を受け取るよ
def ISL(n):
  l=[]*n
  for i in range(n):
    a,b=input().split()
    b=int(b)
    l[i]=[a,b]
  return l
