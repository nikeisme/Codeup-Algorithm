# 10*10 크기의 미로 상자의 구조와 먹이의 위치가 입력된다.

# 성실한 개미가 이동한 경로를 9로 표시해 출력한다.

m=[]
for i in range(12) :
  m.append([])
  for j in range(12) :
    m[i].append(0)

for i in range(10) :
  a=input().split()
  for j in range(10) :
    m[i+1][j+1]=int(a[j])

x = 2
y = 2
while True :
  if m[x][y] == 0 :
    m[x][y] = 9
  elif m[x][y] == 2 :
    m[x][y] = 9
    break

  if (m[x][y+1]==1 and m[x+1][y]==1) or (x==9 and y==9) :
    break

  if m[x][y+1] != 1 :
    y += 1
  elif m[x+1][y] != 1 :
    x += 1
    

for i in range(1, 11) :
  for j in range(1, 11) :
    print(m[i][j], end=' ')
  print()