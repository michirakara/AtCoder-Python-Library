#セグ木だよ
from pyclbr import Function

class SegTree:
  def __init__(self,l:list,func:Function,id_el):
    #初期化
    self.func=func
    self.id_el=id_el
    self.n=1<<(len(l)-1).bit_length()
    self.dat=[id_el]*2*self.n
    for i in range(len(l)):
      self.dat[self.n+i]=l[i]
    
    for i in range(self.n-1,0,-1):
      self.dat[i]=self.func(self.dat[2*i],self.dat[2*i+1])
  
  def update(self,k,x):
    #l[k]をxにする
    k+=self.n
    self.dat[k]=x
    while k>1:
      self.dat[k>>1]=self.func(self.dat[k],self.dat[k^1])
      k>>=1
  
  def query(self,l:int,r:int):
    #[l,r)のfunc
    out=self.id_el
    l+=self.n
    r+=self.n
    while l<r:
      if l&1:
        out=self.func(out,self.dat[l])
        l+=1
      if r&1:
        out=self.func(out,self.dat[r-1])
      l>>=1
      r>>=1
    return out

def func(x,y):
  #随時変更エリア
  return min(x,y)
