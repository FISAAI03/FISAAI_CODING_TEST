n = int(input())
net = int(input())
connect = []

for _ in range(net):
    connect.append(list(map(int, input().split())))

# stack을 활용하기 위해 네트워크로 연결된 바이러스가 걸린 컴퓨터 저장 set(중복방지) 설정
virus_com = set({1})
cnt = 0

# stack에 원소(바이러스가 걸린 컴퓨터터)가 없을 때까지 반복
while virus_com:
    vc = virus_com.pop()
    cnt += 1
    for i in connect[:]:
        if vc == i[0]:
            virus_com.add(i[1])
            connect.remove(i)
        elif vc == i[1]:
            virus_com.add(i[0])
            connect.remove(i)

print(cnt-1)
