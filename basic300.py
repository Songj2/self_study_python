##print
#001
print("Hello World")

#002
print("Mary's consemetics")

#003
print("신씨가 소리질렀다. \"도둑이야\".")

#004
print('"C:\\Windows"')

#005
\t는 탭, \n은 줄바꿈

#006
print("오늘은", "일요일")
-> 한칸 뛰고 연속출력

#007
print("naver;kakao;samsung")
print("naver", "kakao", "samsung", sep=";")

#008
print("naver/kakao/samsung")
 print("naver", "kakao", "samsung", sep="/")

 #009
 print("first", end=" ");print("second")

 #010
 print(5/3)


 ##변수
 #011
 s= 50000
 print(s* 10)
 #s= 50000
 #t= s* 10
 #print(t)

 #012_바인
t= 289000000000000
n= 50000
p= 15.79
print(t, type(t))
print(n, type(n))
print(p, type(p))

#013
s= "hello"
t= "python"
print(s+ "!", t)

#014
->8

#015
a= "132"
print(a, type(a))
->문자열

#016
num_str= "720"
print(int(num_str))

#017
num= 100
num_s= str(num)
print(num_s, type(num_S))

#018
str= "15.79"
str_f= float(str)
print(str_f, type(str_f))

#019
year= "2020"
year_n= int(year)
print(year_n, year_n-1, year_n-2)

#020
ac_m= 48584
total= ac_m*36
print(total)

##문자열
#021
letters= 'python'
print(letters[0], letters[2])

#022
license_plate= "24가 2210"
print(license_plate[4: ])
#license_plate= "24가 2210"
#print(license_plate[-4: ])
---> '-'는 뒤에서 부터를 의미

#023
string= "홀짝홀짝홀짝"
print(string[::2])
---> [시작인덱스:끝인덱스:오프셋]

#024
string= "PYTHON"
print(string[::-1])

#025
phone_number= "010-1111-2222"
sp_num= phone_number.split("-")
print(sp_num[0], sp_num[1], sp_num[2])
#phone_number = "010-1111-2222"
#phone_number1 = phone_number.replace("-", " ")
#print(phone_number1)

#026
phone_number= "010-1111-2222"
sp_num= phone_number.replace("-", "")
print(sp_num)

#027
url = "http://sharebook.kr"
print(url[-2:])
#url_sp= url.split(".")
#print(url_sp[-1])

#028
->Python
#오류, 문자열은 수정 불가

#029
string=  'abcdfe2a354a32a'
str_re= string.replace("a", 'A')
print(str_re)

#030
-> abcd

#031
->34

#032
->HiHiHi

#033
print("-"*80)

#034
t1= 'python'
t2= 'java'

sum= t1 +" "+  t2 + " "
print(sum*4)

#035
name1= "김민수"
age1= 10
name2= "이철희"
age2= 13
print("이름: %s 나이: %d \n이름: %s 나이: %d"  %(name1, age1, name2, age2))

#036
print("이름: {0} 나이: {1} \n이름: {2} 나이: {3}".format(name1, age1, name2, age2))

#037
print(f"이름: {name1} 나이: {age1} \n이름: {name2} 나이: {age2}")

#038
s= "5,969,782,550"
s_re= int(s.replace(",", ""))
print(s_re, type(s_re))

#039
q= "2020/03(E) (IFRS연결)"
q_sl= q.split("(")
print(q_sl[0])
#print(q[:7])

#040
data= "  삼성전자  "
print(data.strip())

#041
ticker = "btc_krw"
print(ticker.upper())

#042
ticker = "BTC_KRW"
print(ticker.lower())

#043
s= "hello"
print(s.capitalize())

#044_T/F 출력
file_name = "보고서.xlsx"
print(file_name.endswith('xlsx'))

#045
print(file_name.endswith('xlsx') or file_name.endswith("xls"))
#file_name.endswith(("xlsx", "xls"))

#046_T/F 출력
file_name = "2020_보고서.xlsx"
print(file_name.startswith('2020'))

#047
a = "hello world"
print(a.split())

#048
ticker = "btc_krw"
print(ticker.split("_"))

#049
date = "2020-05-01"
print(date.split('-'))

#050
data = "039490     "
print(data.rstrip())

##리스트
#051(~055)
movie_rank=["닥터 스트레인지", "스플릿", "럭키"]

#052
movie_rank.append("배트맨")

#053
movie_rank.insert(1, "슈퍼맨")

#054
del movie_rank[3]

#055
del movie_rank[2:]
#del movie_rank[2]
#del movie_rank[2]

#056
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
langs= lang1+lang2
print(langs)

#057
nums = [1, 2, 3, 4, 5, 6, 7]
print(f"max: {max(nums)}\nmin: {min(nums)}")

#058
nums = [1, 2, 3, 4, 5]
print(sum(nums))

#059
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "쏘세지", "라면", "팥빙수", "김치전"]
print(len(cook))

#060
nums = [1, 2, 3, 4, 5]
print(sum(nums)/len(nums))

#061_슬라이싱
price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])

#062
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[::2])

#063
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[1::2])

#064
nums = [1, 2, 3, 4, 5]
print(nums[::-1])

#065
interest = ['삼성전자', 'LG전자', 'Naver']
print(interest[0], interest[2], sep=" ")

#066(~068)
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
result= " ".join(interest)
print(result)
#print(" ".join(interest))

#067
print("/".join(interest))

#068
print("\n".join(interest))

#069
string = "삼성전자/LG전자/Naver"
interest= string.split("/")
print(interest)

#070
data = [2, 4, 3, 1, 5, 10, 9]
#data.sort()    #data2= sorted(data)
#print(data)    #print(data2)


##튜플
#071
my_variable= ()
#print(type(my_variable))

#072
movie_rank= ('닥터 스트레인지', '스플릿', '럭키')

#073
t= (1, ) #하나의 데이터를 저장할 때 쉼표 입력
print(t, type(t))

#074
-> 튜플은 수정할 수 없는 데이터타입인데 값을 수정하려고 해

#075
-> int타입
-----> tuple타입. 괄호 생략하고 튜플로 정의 가능

#076
-> 튜플은 수정 불가
t= ('a', 'b', 'c')
t= ('A', 'B','C')
print(t)

#077
interest = ('삼성전자', 'LG전자', 'SK Hynix')
inter= list(interest)
print(inter)

#078
interest = ['삼성전자', 'LG전자', 'SK Hynix']
inter= tuple(interest)
print(inter)

#079
-> apple banana cake

#080
data= tuple(range(2, 100, 2))
print(data)


##딕셔너리
#081(~083)
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
*valid_score, b, c= scores
print(valid_score)

#082
a, b, *valid_score= scores
print(valid_score)

#083
a, *valid_score, b= scores
print(valid_score)

#084
temp= {}
print(type(temp))

#085
ice= {"메로나":1000, "폴라포":1200, "빵빠레": 1800}
print(ice)

#086_몰랐음
ice["죠스바"]= 1200
ice["월드콘"]= 1500
print(ice)

#087(~089)
ice = {'메로나': 1000,
       '폴로포': 1200,
       '빵빠레': 1800,
       '죠스바': 1200,
       '월드콘': 1500}
print( "메로나 가격: %d" %ice['메로나'])

#088
ice["메로나"]= 1300

#089
del ice["메로나"]

#090
-> 딕셔너리에 존재하지 않는 값을 호출해서

#091(~094)
inventory={'메로나':[300, 20], '비비빅':[400, 3], '죠스바':[250, 100]}
print(inventory)

#92
print("%d 원"%inventory['메로나'][0])

#93
print("%d 개"%inventory['메로나'][1])

#094
inventory["월드콘"]= [500, 7]

#095(~098)
icecream= {'탱크보이':1200, '폴라포':1200, '빵빠레':1800, '월드콘':1500, '메로나':1000}

print(icecream.keys())
#ice= list(icecream.keys())
#print(ice)

#096
price= list(icecream.values())
print(price)

#097
price= list(icecream.values())
print(sum(price))
#print(aum(icecream.values()))

#098
new_product= {'팥빙수': 2700, '아맛나':1000}

icecream.update(new_product)
print(icecream)

#099_모른다
keys= ('apple', 'pear', 'peach')
vals= (300, 250, 400)

result= dict(zip(keys, vals))
print(result)

#100
data= ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price= [10500, 10300, 10100, 10800, 11000]

close_table= dict(zip(data, close_price))
print(close_table)

##분기문
#101
-> boolean타입

#102(~105)
-> false
-> true
-> true
-> true

#106(~110)
-> 기호의 순서가 잘못됨, >=
-> 공백
->Hi, there.
-> 4 #1 2 4
-> 3 5

#111
str= input()
print(str*2)

#112
num= input("숫자를 입력하세요: ")
print(int(num)+10)

#113
num= int(input("숫자를 입력하세요: "))
if(num%2==0):
    print("짝수")
else:
    print("홀수")

#114
num= int(input("입력값: "))
if (num+20)>255:
    print(255)
else:
    print(num+20)

#115
num= int(input("입력값: "))
if (num-20)>255:
    print(255)
elif(num-20)<0:
    print(0)
else:
    print(num-20)

#116
time= input("현재시간: ")
sltime= time.split(":")
if sltime[1]=="00":
#if time[-2: ]== "00":
    print('정각입니다.')
else:
    print("정각이 아닙니다.")

#117
infruit= input("좋아하는 과일은? ")
fruit= ["사과", "포도", "홍시"]

if infruit in fruit:
    print("정답입니다.")
else:
    print("오답입니다.")

#118
warn_investment_list= ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
user= input()

if user in warn_investment_list:
    print("투자 경고 종목입니다.")
else:
    print("투자 경고 종목이 아닙니다.")

#119
fruit= {"봄":"딸기", "여름":"토마토", "가을":"사과"}
inseason= input("제가 좋아하는 계절은: ")

if inseason in fruit.keys(): #.keys() 생략가능
    print("정답입니다.")
else:
    print("오답입니다.")

#120
inseason= input("제가 좋아하는 과일은: ")

if inseason in fruit.values():
    print("정답입니다.")
else:
    print("오답입니다.")
    
#121
str= input()
if str.islower() == True:
#if str.islower():
    print(str.upper())
else:
    print(str.lower())

#122
score= int(input())

if 100>=  score >=81:
    print("A")
elif 80>= score >=61:
    print("B")
elif 60>= score >=41:
    print("C")
elif 40>= score >=21:
    print("D")
else:
    print("E")

#123_틀린건 아니지만 코드가 구림
price= input("입력: ")
list= price.split()

if list[1]== "달러":
    result= float(list[0])*1167
    print("%.2f 원"%result)
elif list[1]== "엔":
    result= float(list[0])*1.096
    print("%.2f 원"%result)
elif list[1]== "유로":
    result= float(list[0])*1268
    print("%.2f 원"%result)
elif list[1]== "위안":
    result= float(list[0])*171
    print("%.2f 원"%result)
else:
    print("잘못 입력했습니다.")
    
#환율= {"달러":1167, "엔":"1.096, "유로":"1268, "위안":"171}
#inNum= input("입력: ")
#num, currency= inNum.split()
#print(float(num)* 환율[currency], "원")

#124
num1= int(input("input number1: "))
num2= int(input("input number2: "))
num3= int(input("input number3: "))

if num1>num2:
    if num1>num3:
        print(num1)
    elif num3>num2:
        print(num3)
    else:
        print(num2)
elif num2>num3:
    print(num2)
else :
    print (num3)

#if num1> num2 and num1> num3:
#    print(num1)
#elif num2> num1 and num2> num3:
#   print(num2)
#else:
#   print(num3)

#125
numDict= {'011':"SKT", '016':"KT", '019':"LGU", '010':"알수 없음"}
tel= input("휴대전화 번호 입력: ")
num= tel[:3:]

if num in numDict:
    print("당신은 %s 사용자 입니다." %numDict[num])

#126
adNum= input("우편 번호 입력: ")
spNum= adNum[:3:]

if spNum == '010' or spNum =='011' or spNum == '012' : #if spNum in ['010', '011', '012']:
    print('강북구')
elif spNum =='o13' or spNum == '014' or spNum == '015':
    print('도봉구')
elif spNum== '016' or spNum =='017' or spNum =='018' or spNum =='019':
    print('노원구')
else:
    print('잘못된 번호입니다,')

#127
inNum, getNum= input("주민등록번호: ").split('-')

if int(getNum[0]) in [1,3]:
    print("남자")
elif int(getNum[0]) in [2, 4]:
    print("여자")
else:
    print("잘못된 정보입니다,")

#128
    inNum= input("주민등록번호: ")

getNum= inNum.split('-')[1]
print(getNum[1:3])
if getNum[1:3] in ['00', '01', '02', '03', '04', '05', '06', '07', '08']:
#if 0<= int(getNum[1:3]) <= 8:
    print('서울입니다.')
else:
    print('서울이 아닙니다.')

#129
fnum, lnum= input("주민등록번호: ").split('-')

cal1= (int(fnum[0])*2+ int(fnum[1])*3+ int(fnum[2])*4+ int(fnum[3])*5+ int(fnum[4])*6+ int(fnum[5])*7+
       int(lnum[0])*8+ int(lnum[1])*9+ int(lnum[2])*2+ int(lnum[3])*3+ int(lnum[4])*4+ int(lnum[5])*5)%11
cal2= 11-cal1

if lnum[6] ==cal2:
    print('유효한 주민등록번호입니다.')
else:
    print('유효하지 않은 주민등록번호입니다.')

#130
import requests
btc= requests.get("https://api.bithumb.com/public/ticker/").json()['data']

fluct= float(btc['max_price']) - float(btc['min_price'])
stPrice= float(btc['opening_price'])
mxPrice= float(btc['max_price'])

if  stPrice+ fluct> mxPrice:
    print('상승장')
else:
    print('하락장')

##반복문
#131
-> 사과\n귤\n수박
-> 사과\n귤\n수박 # #####\n#####\n#####

#133
print("A")
print("B")
print("C")

#134
print("출력: A")
print("출력: B")
print("출력: C")

#135
b= 'A'
print('변환: ', b.lower())
b= 'B'
print('변환: ', b.lower())
b= 'C'
print('변환: ', b.lower())

#136
for c in [10, 20, 30]:
    print(c)

#137
c= [10, 20, 30]
for i in c:
    print(c)

#138
for c in [10, 20, 30]:
    print("-----")

#139
print('+++++')
for c in [10, 20, 30]:
    print(c)

#140
for i in range(0, 4):
#for i in [1, 2, 3, 4]
    print('------')

#141
price= [100, 200, 300]
for i in price:
    print(i+10)

#142
menu= ['김밥', '라면', '튀김']
for i in menu:
    print('오늘의 메뉴: ', i)

#143
coop= ["SK하이닉스", "삼성전자","LG전자"]
for i in coop:
    print(len(i))

#144
animal= ['dog', 'cat', 'parrot']
for i in animal:
     print(i, len(i))

#145
for i in animal:
     print(i[0])

#146
num= [1, 2, 3]
for i in num:
    print('3 x', i)
    
#147
for i in num:
    print('3 x', i ,"=", int(i)*3)
    #print('3 x {} = {}'.format(i, i*3)

#148
strl=['가', '나', '다', '라']
for i in range(1,4):
    print(strl[i])
#for i in strl[1:]:
    #print(i)

#149
for i in strl[0::2]:
    print(i)

#150
for i in strl[::-1]:
    print(i)

#151
nums= [3, -20, -3, 44]
for i in nums:
    if i< 0:
        print(i)

#152
nums= [3, 100, 23, 44]
for i in nums:
    if i% 3== 0:
        print(i)

#153
nums= [13, 21, 12, 14, 30, 18]
for i in nums:
    if i% 3== 0 and i< 20:
        print(i)

#154
strl= ["I", "study", "python", "language", "!"]
for i in strl:
    if len(i)>= 3:
        print(i)
    
#155
strl= ["A", "b", "c", "D"]
for i in strl:
    if i.isupper():
        print(i)

#156
for i in strl:
    if i.islower():
    #if not i.upper():
        print(i)

#157
strl= ['dog', 'cat', 'parrot']
for i in strl:
    print(i[0].upper()+i[1:])

#158
strl= ['hello.py', 'ex01.py', 'intro.hwp']
for i in strl:
    print(i.split('.')[0])

#159
strl= ['intra.h', 'intra.c', 'define.h', 'run.py']
for i in strl:
    if i.split('.')[1]== 'h':
        print(i)

#160
for i in strl:
    if i.split('.')[1]== 'h' or i.split('.')[1]== 'c':
        print(i)

#161
for i in range(0,100):
    print(i)

#162
for i in range(2002,2051,4):
    print(i)

#163
for i in range(3, 31, 3):
    print(i)

#164
for i in range(99, -1, -1):
    print(i)
#for i in range(100):
    #print(99-i)

#165
for i in range(0, 10):
    print('0.',i)
#for i in range(10):
    #print(i/10, i)

#166
for i in range(1,10):
    print('3 x {}= {}'.format(i, i*3))

#167
for i in range(1,10,2):
    print('3 x {}= {}'.format(i, i*3))

#168
sum= 0
for i in range(1,11):
    sum+= i
print("합:", sum)

#169
sum= 0
for i in range(1,11,2):
    sum+= i
print("합:", sum)

#170
acc= 1
for i in range(1,11):
    acc*= i
print("곱:", acc)

#171
price_list = [32100, 32150, 32000, 32500]
for i in range(len(price_list)):
    print(price_list[i])

#172
for i in range(len(price_list)):
    print(i, price_list[i])
#for i, data in enumerate(price_list):
    #print(i, data)

#173
for i in range(len(price_list)):
    print((len(price_list)- 1) -i, price_list[i])

#174
for i in range(1, len(price_list)):
    print(90+ i* 10), price_list[i])

#175
my_list = ["가", "나", "다", "라"]
for i in range(len(my_list)-1):
    print(my_list[i], my_list[i+1])

#176
my_list = ["가", "나", "다", "라", "마"]
for i in range(len(my_list)-2):
    print(my_list[i], my_list[i+1], my_list[i+2])

#177
my_list = ["가", "나", "다", "라"]
for i in range(len(my_list)-1):
    print(my_list[3-i], my_list[2-i])

#178
my_list = [100, 200, 400, 800]
for i in range(len(my_list)-1):
    print(my_list[i+1]- my_list[i])

#179
my_list = [100, 200, 400, 800, 1000, 1300]
for i in range(len(my_list)-2):
    print((my_list[i]+ my_list[i+1]+ my_list[i+2])/3)
#for i in range(1, len(my_list) - 1):
    #print(abs(my_list[i-1] + my_list[i] + my_list[i+1]) / 3)

#180
low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]
volatility=[]

for i in range(5):
    volatility.append( high_prices[i]-low_prices[i])

#181
apt= [[101, 102], [201, 202], [301,302]]

#182
stock=[["시가", 100, 200, 300], ["종가", 80, 210, 330]]

#183
stock={'시가':[100, 200, 300], '종가':[80, 210, 330]}

#184
stock={'10/10': [80, 110, 70, 90], '10/11': [210, 230, 190, 200]}

#185
apart = [ [101, 102], [201, 202], [301, 302] ]
for i in apart:
    for j in i:
        print(j, '호')

#186
for i in range(len(apart)):
    for j in range(2):
        print(apart[2-i][j], '호')
#for i in apart[::-1]:
    #for j in i:
        #print(j, '호')

#187
for i in range(len(apart)):
    for j in range(2):
        print(apart[2-i][j-1], '호')
#for i in apart[::-1]:
    #for j in i[::-1]:
        #print(j, '호')

#188
for i in apart:
    for j in i:
        print(j, '호');print("-----")

#189
for i in apart:
    for j in i:
        print(j, '호')
    print("-----")

#190
for i in apart:
    for j in i:
        print(j, '호')
print("-----")

#191 ??문제 오류?
data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]
for i in data:
    for j in i:
        print(j*1.014)

#192
for i in data:
    for j in i:
        print(j*1.014)
    print("-"*4)

#193
result=[]
for i in data:
    for j in i:
        result.append(j*1.014)

#194
result=[]
for i in data:
    row=[]
    for j in i:
        row.append(j*1.014)
    result.append(row)

#195
for i in ohlc[1:]:
    #print([3])
    for j in i[-1:]:
        print(j)

#196
for i in ohlc[1:]:
    if i[3]>150:
        print(i[3])

#197
for i in ohlc[1:]:
    if i[3]>= i[0]:
        print(i[3])

#198
volatility=[]
for i in ohlc[1:]:
    volatility.append(i[1]-i[2])

#199
for i in ohlc[1:]:
    if i[3]>i[0]:
        print(i[1]-i[2])

#200
sum=0
for i in ohlc[1:]:
    sum+=(i[0]-i[3])
    
##함수
#201
def print_coin():
    print('비트코인')

#202
print_coin()

#203
#for i in range(100):
    #print_coin()

#204
def print_coin():
    for i in range(100):
        print('비트코인')

#205
-> 정의되지 않은 함수를 먼저 호출해서.

#206
->A\n B\n C\n A\n B\n

#207
->A\n C\n B

#208
->A\n C\n B\n E\nD

#209
->B\n A

#210
-> B\n C\n B\n C\nB\n C\n A

#211
-> 안녕\n Hi

#212
-> 7 \n15

#213
-> 매개변수가 필요한 함수를 호출하는데 매개변수를 입력하지 않아
#214
-> 변수의 타입이 달라

#215
def print_with_smile(a):
    print(a,':D')

#216
print_with_smile("안녕하세요")

#217
def  print_upper_price(price):
    print(price*1.3)

#218
def  print_sum(a, b):
    print(a+b)

#219
def  print_arithmetic_operation(a, b):
    print('{} + {}= {}'.format(a, b, a+b))
    print('{} - {}= {}'.format(a, b, a-b))
    print('{} * {}= {}'.format(a, b, a*b))
    print('{} / {}= {}'.format(a, b, a/b))

#220
def print_max(a, b, c):
    if( a>b and a>c):
        print(a)
    elif(b>a and b>c):
        print(b)
    elif (c>a and c>b):
        print(c)
    else:
        print('error;')

#221
def print_reverse(string):
    print(string[::-1])

#222
def print_score (score):
    sum=0
    for i in score:
        sum+= i
    print(sum/len(score))
    #print(sum(score)/len(score))

#223
def print_even (nums):
    for i in nums:
        if i% 2== 0:
            print(i)

#224
def print_keys  (dic):
    key= list(dic.keys())
    for i in key:
        print(i)
    #for i in dic.keys():
        #print(i)

#225
my_dict = {"10/26" : [100, 130, 100, 100],
           "10/27" : [10, 12, 10, 11]}

def print_value_by_key  (dic, string):
    print(dic[string])

#226
def print_5xn(string):
    count=0
    st=""
    for i in string:
        if count<5:
            count+=1
            st+=i
        else:
            print(st)
            count=1
            st=i
    print(st)
    #count= int(len(string)/ 5)
    #for i in range(count+1):
        #print(string[i * 5: i* 5+5])\

#227
def printmxn(string, num):
    for i in range(num+1):
        print(string[i*int(num): i* int(num)+ int(num)])
    
#228
def calc_monthly_salary(annual_salary):
    print(int(annual_salary)/12)
    #monthly_pay= int(annual_salary)/12
    #retrun monthly_pay

#229
-> 왼쪽: 100\n 오른쪽: 200

#230
-> 오류 발생, 매개변수의 순서와 이름이 맞지 않
#왼쪽: 200\n 오른쪽: 100

#231
-> 오류 발생

#232
def make_url(word):
    return "www." + string + ".com"

#233
def make_list(lis):
    mklist= []
    for i in lis:
        mklist.append(i)
    return mklist
    #return list(lis)

#234
def pickup_even(nums):
    even_list= []
    for i in nums:
        if i% 2== 0:
            even_list.append(i)
    return even_list

#235
def convert_int(nums):
    num= ""
    for i in nums.split(","):
        num+=i
    return num
    #retrun int(nums.replace(',', ''))

#236
-> 22

#237
-> 22

#238
-> 140

#239
-> 16

#240
-> 28

##모듈
#241
import datetime
datetime.datetime.today()

#242
print(datetime.datetime.now(), type(datetime.datetime.now()))

#243
#now = datetime.datetime.now()

#for day in range(5, 0, -1):
    #delta = datetime.timedelta(days=day)
    #date = now - delta
    #print(date)

#244
import datetime

now= datetime.datetime.now()
print(now.strftime("%H:%M:%S"))

#245
import datetime

date= "2020-05-04"
print(datetime.datetime.strptime(date, "%Y-%m-%d"))

#246
import datetime
from time import sleep

for i in range(7):
    sleep(1)
    print(datetime.datetime.now())

#247
-> import 모듈/ from 모듈 import 함수/ from 모듈 import */from 모듈 as 별칭

#248
import os

os.getcwd()

#249
import os

os.rename("파일경로/파일이름.파일유형", '=>', "경로/변경할 파일이름.파일유형")

#250
import numpy as np

np.arange(0, 5, 0.1)

##클래스
#251
-> 클래스: 필요한 객체를 생성 객체: 생성된 객체 인스턴스: ==객

#252_ 클래스 정의
class Human:
    pass

#253_ 인스턴스 생성
Human(areum)
#areum= Human()

#254_생성자
class Human:
    #def __init__(self):
    print("응애응애")

#255
class Human:
    def __init__(self, name, age, sex):
        self.name= name
        self.age= age
        self.sex= sex

#256
print(areum.name, areum.age, areum.sex)

#257_ 메소드
class Human:
    def __init__(self, name, age, sex):
        self.name= name
        self.age= age
        self.sex= sex

    def who(cls):
        print('이름: {}, 나이: {}, 성별: {}'.format(cls.name, cls.age, cls.sex))
        
areum = Human("아름", 25, "여자")
areum.who()

#258
class Human:
    def __init__(self, name, age, sex):
        self.name= name
        self.age= age
        self.sex= sex

    def who(cls):
        print('이름: {}, 나이: {}, 성별: {}'.format(cls.name, cls.age, cls.sex))

    def setInfo(self, name, age, sex):
        self.name= name
        self.age= age
        self.sex= sex
        
areum = Human("모름", 0, "모름")
areum.who()
areum.setInfo("아름", 25, "여자")
areum.who()

#259
class Human:
    def __init__(self, name, age, sex):
        self.name= name
        self.age= age
        self.sex= sex

    def who(cls):
        print('이름: {}, 나이: {}, 성별: {}'.format(cls.name, cls.age, cls.sex))

    def setInfo(self, name, age, sex):
        self.name= name
        self.age= age
        self.sex= sex

    def __del__(self):
        print('나의 즉음을 알리지 말라')
        
areum= Human("아름", 25, "여자")
del areum

#260_
-> 기존에 정의된 함수를 메소드 이름으로 사용해
#정의한 함수에 매개변수 self를 작성하지 않아서 

#261
class Stock:
    pass

#262
class Stock:
    def __init__(self, company, code):
        self.company= company
        self.code= code

#263
class Stock:
    def __init__(self, company, code):
        self.company= company
        self.code= code

    def set_name(self, company):
        self.company= company

ss= Stock("삼성전자", "005930")
ss.set_name("samsung")
print(ss.company, ss.code)

#264
class Stock:
    def __init__(self, company, code):
        self.company= company
        self.code= code

    def set_name(self, company):
        self.company= company

    def set_code(self, code):
        self.code= code
        
ss= Stock("삼성전자", "005930")
ss.set_name("samsung")
ss.set_code("112234")
print(ss.company, ss.code)

#265
class Stock:
    def __init__(self, company, code):
        self.company= company
        self.code= code

    def set_name(self, company):
        self.company= company

    def set_code(self, code):
        self.code= code

    def get_name(self):
        return self.company

    def get_code(self):
        return self.code
    
ss= Stock("삼성전자", "005930")
print(ss.get_name())
print(ss.get_code())

#266
class Stock:
    def __init__(self, name, code, per, pbr,  yie):
        self.name= name
        self.code= code
        self.per= per
        self.pbr= pbr
        self.yie= yie

    def set_name(self, name):
        self.name= name

    def set_code(self, code):
        self.code= code

    def get_name(self):
        return self.name

    def get_code(self):
        return self.code

#267
ss= Stock("삼성전자", "005930", 15.79, 1.33, 2.83)

#268
class Stock:
    def __init__(self, name, code, per, pbr,  yie):
        self.name= name
        self.code= code
        self.per= per
        self.pbr= pbr
        self.yie= yie

    def set_name(self, name):
        self.name= name

    def set_code(self, code):
        self.code= code

    def set_per(self, per):
        self.per= per

    def set_pbr(self, pbr):
        self.pbr= pbr

    def set_yie(self, yie):
        self.yie= yie

    def get_name(self):
        return self.name

    def get_code(self):
        return self.code

#269
ss= Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
ss.set_per(12.75)
print(ss.per)

#270
ss= Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
hd= Stock("현대차", "005380", 8.7, 0.35, 4.27)
lg= Stock("LG전자", "066570", 317.34, 0.69, 1.37)

stList= [ss.name, ss.code, ss.per, ss.pbr, ss.yie,
         hd.name, hd.code, hd.per, hd.pbr, hd.yie,
         lg.name, lg.code, lg.per, lg.pbr, lg.yie,]

for i in range(1, len(stList)+1, 5):
    print(stList[i], stList[i+1])

#stList= []
#stList.append(ss)
#stList.append(hd)
#stList.append(lg)

#for i in stList:
    #print(i.code, i,per)

#271
class Account:
    def __init__(self, name, bal):
        self.name= name
        self.bal= bal
        self.bank= "SC은행"
        accNum= "123-12-123456"
        
#import random

#class Account:
    #def __init__(self, name, bal):
        #self.name= name
        #self.bal= bal
        #self.bank= "SC은행"

        #num1= random.randint(0, 999)
        #num2= random.randint(0, 99)
        #num3= random.randint(0, 999999)

        #num1= str(num1).zfill(3)
        #num2= str(num2).zfill(2)
        #num3= str(num3).zfill(6)

        #self.accNum= num1+ '-'+ num2+ '-'+ num3

#272
import random

class Account:
    count= 0
    
    def __init__(self, name, bal):
        self.name= name
        self.bal= bal
        self.bank= "SC은행"

        num1= random.randint(0, 999)
        num2= random.randint(0, 99)
        num3= random.randint(0, 999999)

        num1= str(num1).zfill(3)
        num2= str(num2).zfill(2)
        num3= str(num3).zfill(6)

        self.accNum= num1+ '-'+ num2+ '-'+ num3
        self.count+= 1
        
kim = Account("김민수", 100)
print(kim.count)
 
#273
import random

class Account:
    count= 0
    
    def __init__(self, name, bal):
        self.name= name
        self.bal= bal
        self.bank= "SC은행"

        num1= random.randint(0, 999)
        num2= random.randint(0, 99)
        num3= random.randint(0, 999999)

        num1= str(num1).zfill(3)
        num2= str(num2).zfill(2)
        num3= str(num3).zfill(6)

        self.accNum= num1+ '-'+ num2+ '-'+ num3
        self.count+= 1
        
    def get_account_num(cls):
        print(cls.count)

kim = Account("김민수", 100)
print(kim.get_account_num())

#274
import random

class Account:
    count= 0
    
    def __init__(self, name, bal):
        self.name= name
        self.bal= bal
        self.bank= "SC은행"

        num1= random.randint(0, 999)
        num2= random.randint(0, 99)
        num3= random.randint(0, 999999)

        num1= str(num1).zfill(3)
        num2= str(num2).zfill(2)
        num3= str(num3).zfill(6)

        self.accNum= num1+ '-'+ num2+ '-'+ num3
        self.count+= 1
        
    def get_account_num(cls):
        print(cls.count)

    def deposit(cls, amount):
        if amount>=1:
            cls.bal+= amount
        else:
            print('금액을 제대로 입력하세요.')

kim = Account("김민수", 100)
kim.deposit(50)
kim.bal

#275
import random

class Account:
    count= 0
    
    def __init__(self, name, bal):
        self.name= name
        self.bal= bal
        self.bank= "SC은행"

        num1= random.randint(0, 999)
        num2= random.randint(0, 99)
        num3= random.randint(0, 999999)

        num1= str(num1).zfill(3)
        num2= str(num2).zfill(2)
        num3= str(num3).zfill(6)

        self.accNum= num1+ '-'+ num2+ '-'+ num3
        self.count+= 1
        
    def get_account_num(cls):
        print(cls.count)

    def deposit(self, amount):
        if amount>=1:
            slef.bal+= amount
        else:
            print('금액을 제대로 입력하세요.')

    def withdraw(self, amount):
        if self.bal> amount:
            self.bal-= amount
        else:
            print("잔액이 부족합니다.")
            
kim = Account("김민수", 100)
kim.withdraw(50)
kim.bal

#276
import random

class Account:
    count= 0
    
    def __init__(self, name, bal):
        self.name= name
        self.bal= bal
        self.bank= "SC은행"

        num1= random.randint(0, 999)
        num2= random.randint(0, 99)
        num3= random.randint(0, 999999)

        num1= str(num1).zfill(3)
        num2= str(num2).zfill(2)
        num3= str(num3).zfill(6)

        self.accNum= num1+ '-'+ num2+ '-'+ num3
        self.count+= 1
        
    def get_account_num(cls):
        print(cls.count)

    def deposit(self, amount):
        if amount>=1:
            self.bal+= amount
        else:
            print('금액을 제대로 입력하세요.')

    def withdraw(self, amount):
        if self.bal> amount:
            self.bal-= amount
        else:
            print("잔액이 부족합니다.")

    def  display_info(self):
        print("은행 이름: {}\n 예금주: {}\n 계좌번호: {}".format(self.bank, self.name, self.accNum))
        print("잔고: {:,}".format(self.bal))

#277
import random

class Account:
    count= 0
    incount= 0
    
    def __init__(self, name, bal):
        self.name= name
        self.bal= bal
        self.bank= "SC은행"

        num1= random.randint(0, 999)
        num2= random.randint(0, 99)
        num3= random.randint(0, 999999)

        num1= str(num1).zfill(3)
        num2= str(num2).zfill(2)
        num3= str(num3).zfill(6)

        self.accNum= num1+ '-'+ num2+ '-'+ num3
        self.count+= 1
        
    def get_account_num(cls):
        print(cls.count)

    def deposit(self, amount):
        if amount>=1:
            self.bal+= amount
            self.incount+=1

            if self.incount==5:
                self.bal*=1.01
                self.incount=0
                
        else:
            print('금액을 제대로 입력하세요.')

    def withdraw(self, amount):
        if self.bal> amount:
            self.bal-= amount
        else:
            print("잔액이 부족합니다.")

    def  display_info(self):
        print("은행 이름: {}\n 예금주: {}\n 계좌번호: {}".format(self.bank, self.name, self.accNum))
        print("잔고: {:,}".format(self.bal))

#278
kim = Account("김민수", 100)
choi= Account("최민지", 15000)
park= Account("박민재", 10000000)

customer= []
customer.append(kim)
customer.append(choi)
customer.append(park)

#279
for i in customer:
    if i.bal>=1000000:
        i.display_info()

#280
import random

class Account:
    count= 0
    incount= 0
    deposit_His= []
    withdraw_His= []
    
    def __init__(self, name, bal):
        self.name= name
        self.bal= bal
        self.bank= "SC은행"

        num1= random.randint(0, 999)
        num2= random.randint(0, 99)
        num3= random.randint(0, 999999)

        num1= str(num1).zfill(3)
        num2= str(num2).zfill(2)
        num3= str(num3).zfill(6)

        self.accNum= num1+ '-'+ num2+ '-'+ num3
        self.count+= 1
        
    def get_account_num(cls):
        print(cls.count)

    def deposit(self, amount):
        if amount>=1:
            self.bal+= amount
            self.incount+=1
            self.deposit_His.append(amount)

            if self.incount==5:
                self.bal*=1.01
                self.incount=0
                
        else:
            print('금액을 제대로 입력하세요.')

    def withdraw(self, amount):
        if self.bal> amount:
            self.bal-= amount
            self.withdraw_His.append(amount)
        else:
            print("잔액이 부족합니다.")

    def  display_info(self):
        print("은행 이름: {}\n 예금주: {}\n 계좌번호: {}".format(self.bank, self.name, self.accNum))
        print("잔고: {:,}".format(self.bal))

    def deposit_history(self):
        for i in self.deposit_His:
            print(i)
        
    def withdraw_history(self):
        for i in self.withdraw_His:
            print(i)
        
kim = Account("김민수", 100)

kim.deposit(100000)
kim.deposit(4000)
kim.deposit_history()

#281
class car:
    def __init__(self, wheel, price):
        self.wheel= wheel
        self.price= price

#282
class car:
    def __init__(self, wheel, price):
        self.wheel= wheel
        self.price= price

class bicycle(car):
    pass

#283
class car:
    def __init__(self, wheel, price):
        self.wheel= wheel
        self.price= price

class bicycle(car):
    def __init__(self, wheel, price):
        self.wheel= wheel
        self.price= price

bic= bicycle(2, 400)

#284
class bicycle(car):
    def __init__(self, wheel, price, drivetrain):
        !self.wheel= wheel
        !self.price= price
        #super().__init__(wheel, price) or car.__init__(self, wheel, price)
        self.drivetrain= drivetrain

bic= bicycle(2, 400, "시마노")
print(bic.drivetrain)

#285
class autocar(car):
    def __init__(self, wheel, price):
        super().__init__(wheel, price)

    def info(self):
        print("바퀴수: {}\n가격: {}".format(self.wheel, self.price))

auto= autocar(4, 1000)
auto.info()

#286
class car:
    def __init__(self, wheel, price):
        self.wheel= wheel
        self.price= price

    def info(self):
        print("바퀴수: {}\n가격: {}".format(self.wheel, self.price))

class bicycle(car):
    def __init__(self, wheel, price, drivetrain):
        super().__init__(wheel, price)
        self.drivetrain= drivetrain

class autocar(car):
    def __init__(self, wheel, price):
        super().__init__(wheel, price)

bic= bicycle(2, 400, "시마노")
bic.info()
auto= autocar(4, 1000)
auto.info()

#287
class car:
    def __init__(self, wheel, price):
        self.wheel= wheel
        self.price= price

    def info(self):
        print("바퀴수: {}\n가격: {}".format(self.wheel, self.price))

class bicycle(car):
    def __init__(self, wheel, price, drivetrain):
        super().__init__(wheel, price)
        self.drivetrain= drivetrain

    def info(self):
        print("구동계: ", self.drivetrain)
        
class autocar(car):
    def __init__(self, wheel, price):
        super().__init__(wheel, price)

    


bic= bicycle(2, 400, "시마노")
bic.info()

#288
-> 자식호출 

#289
-> 자식생성

#290
-> 부모생성

##파일 입출력과 예외처리
#291
f= open('매수종목1.txt', 'w')
#f= open('매수종목1.txt', mode= "wt", encoding= "utf-8")
f.write('005930\n005380\n035420')
f.close()

#292
f= open('매수종목2.txt', 'w')
f.write('005930 삼성전자\n005380 현대차\n035420 NAVER')
f.close()

#293
import csv
f= open('매수종목.csv', mode='wt', newline="")
wr= csv.writer(f)
wr.writerow(['종목명', '종목코드','PER'])
wr.writerow(['삼성전자', '005930', '15.79'])
wr.writerow(['NAVER', '035420', '55.82'])
f.close()

#294
f= open('매수종목1.txt', mode='r')

li= []
for i in range(3):
    li.append(f.readline())

#lines= f.readlines()
#codes= []
#for i in lines:
    #code= i.strip()
    #codes.append(code)

#f.close()

#295
f= open('매수종목2.txt', mode='r')
lines= f.readlines()

dic= {}
for i in lines:
    keys, values= i.split()
    dic[keys]=values
    print(keys,":", values)

#296
per = ["10.31", "", "8.00"]

for i in per:
    try:
        print(float(i))
    except:
        print(0)

#297
per = ["10.31", "", "8.00"]
nPer= []
for i in per:
    try:
        nPer.append(i)
    except:
        nPer.append(0)

#298
try:
    print(3/0)
except ZeroDivisionError:
    pass

#299
data = [1, 2, 3]

try:
    for i in range(5):
        print(data[i])
except IndexError as e:
    print(e)

#300
per = ["10.31", "", "8.00"]

try: 
    for i in per:
        print(float(per))
except:
    print('오류가 발생했습니다.')
else:
    print('정상 작동')
finally:
    print('finally 작동')
