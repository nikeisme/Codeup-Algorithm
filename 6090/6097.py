# 모든 막대를 놓은 격자판의 상태를 출력한다.
# 막대에 의해 가려진 경우 1, 아닌 경우 0으로 출력한다.
# 단, 각 숫자는 공백으로 구분하여 출력한다.

h,w = input().split()
h = int(h)
w = int(w)

m = []
for i in range(h+1) :
  m.append([])
  for j in range(w+1) :
    m[i].append(0)

n = int(input())
for i in range(n) :
  l,d,x,y = input().split()
  if int(d)==0 :
    for j in range(int(l)) :
      m[int(x)][int(y)+j] = 1
  else :
    for j in range(int(l)) :
      m[int(x)+j][int(y)] = 1

for i in range(1, h+1) :
  for j in range(1, w+1) :
    print(m[i][j], end=' ')
  print()
