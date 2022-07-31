#一つの値ごとに改行されているn個の要素から成り立つ配列を受け取るよ
import sys
input=sys.stdin.readline
def ILV(n):
  return [int(input()) for i in range(n)]
