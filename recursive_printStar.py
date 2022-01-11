n= int(input())
result= [["*" for j in range(n)] for i in range(n)]

def printSt(num,result):
    third= int(num/3)
    k=0    
    
    for i in range(1,n):
        if third+k<= i <third*2+k:
            d= 0
            
            for j in range(1, n):
                if third +d<= j < third*2+d :
                    result[i][j]= " "
                    if j+1== third*2+d:
                        d+=num
        if third*2+k==i+1:
            k+=num
            
    if num<= 3:
        return result
        
    return printSt(third, result)


for i in printSt(n, result):
	for j in i:
		print(j, end="")
	print()
