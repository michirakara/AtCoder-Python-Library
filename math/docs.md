# IsPrime.py
## IsPrime(n)  
nが素数かどうかを判定して素数の場合はTrue、そうでない場合はFalseを返します。  
ミラーラビンの素数判定法を使っているので、ごく稀(実際に起こることはほとんどありえないですが)に間違った値を返すことがあります。

# PollardsRhoAlgorithm.py
## rho_algorith(n,a,x0)
nの素因数を一つ返します。失敗する場合もあるので $x_0$ を変えて複数回試すことをおすすめします。  
Pollard's rho algorithmは高速なので、ほとんどTLEするようなことは起こりません。
