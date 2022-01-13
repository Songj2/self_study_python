n, k= map(int, input().split())
pack= []
for i in range(n):
    pack.append(list(map(int, input().split())))
pack.sort(key=lambda x:(x[1], x[0])) # 가치순으로 정렬, 같은 가치일 경우 무게가 적은 순으로 정렬

w= 0
v= 0
sumW=0
sumV=0
getInd=[[]for i in range(n-1)]

for i in range(n):
    getInd=[]
    if pack[i][0]<k:
        sumW= pack[i][0]
        sumV= pack[i][1]
        getInd[i].append(i)
    for j in range(n):
        if pack[j][0]+sumW<= k and not j in getInd[i-1]:
            sumW+= pack[j][0]
            sumV+=pack[j][1]
            getInd[i].append(j)
            
    if v<sumV:
        v= sumV   


print(v)
######재귀를 이용해서 풀어보기
