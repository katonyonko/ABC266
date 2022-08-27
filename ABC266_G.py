import io
import sys

_INPUT = """\
6
2 1 1 1
1000000 1000000 1000000 1000000
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  mod=998244353
  R,G,B,K=map(int,input().split())
  #Combination
  F=[1]
  for i in range(R+G+B):
    F.append(F[-1]*(i+1)%mod)
  I=[pow(F[-1],mod-2,mod)]
  for i in range(R+G+B):
    I.append(I[-1]*(R+G+B-i)%mod)
  I=I[::-1]
  print(F[R+B]*I[R]*I[B]*F[R]*I[K]*I[R-K]*F[G+B]*I[G-K]*I[B+K]%mod)