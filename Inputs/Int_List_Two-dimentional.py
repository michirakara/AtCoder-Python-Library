#col行ある二次元配列を受け取るよ
import sys
input=sys.stdin.readline
def ILTD(col):
  return [[*map(int,input().split())] for i in range(col)]
