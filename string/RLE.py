def RLE(l:str):
  if len(l)==0:
    return []
  out=[[l[0],1]]
  for i in range(1,len(l)):
    if l[i]!=l[i-1]:
      out.append([l[i],1])
    else:
      out[-1][1]+=1
  return out
