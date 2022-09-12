#リストを入れるよ
#fold(r)でtable[0,r)の累積和
#fold_(l,r)でtable[l,r)の累積和
class CumulativeSum:
  def __init__(self,table):
    self.table=table.copy()
    for i in range(1,len(self.table)):
      self.table[i]+=self.table[i-1]
  
  def fold(self,r:int):
    if r<0:
      return 0
    return self.table[r-1]
  
  def fold_(self,l:int,r:int):
    if l==0:
      return self.fold(r)
    return self.fold(r)-self.fold(l)
