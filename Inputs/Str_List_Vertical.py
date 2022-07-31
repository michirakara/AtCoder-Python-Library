#n行の文字列の配列を受け取るよ
import sys
input=sys.stdin.readline
def SLV(n):
  return [input().rstrip() for i in range(n)]
