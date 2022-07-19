# 바둑알이 깔려 있는 상황이 19 * 19 크기의 정수값으로 입력된다.
# 십자 뒤집기 횟수(n)가 입력된다.
# 십자 뒤집기 좌표가 횟수(n) 만큼 입력된다. 단, n은 10이하의 자연수이다.


# 십자 뒤집기 결과를 출력한다.

d=[]
for i in range(20) :
  d.append([])
  for j in range(20) : 
    d[i].append(0)

for i in range(19) :
  a = input().split()
  for j in range(19) :
    d[i+1][j+1] = int(a[j])

n = int(input())
for i in range(n) :
  x,y=input().split()
  x=int(x)
  y=int(y)
  for j in range(1, 20) :
    if d[j][y]==0 :
      d[j][y]=1
    else :
      d[j][y]=0

    if d[x][j]==0 :
      d[x][j]=1
    else :
      d[x][j]=0

for i in range(1, 20) :
  for j in range(1, 20) :
    print(d[i][j], end=' ')
  print()
