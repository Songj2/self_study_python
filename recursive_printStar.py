n= int(input())
list=[["*" for j in range(n)] for i in range(n)]

def printStar(row, col, list, way):
    max= len(list)    
    temp= 0
    if row<max and col<max:
        while temp<= max*3:
            if max/3<=row<(max/3)*2 and max/3<=col<(max/3)*2:
                list[row][col]= " "           
            elif way== 1:
                if temp<col<=temp+2  and col%3==1 and row%3==1: 
                    list[row][col]= " "    
            temp+=3 
            
        if row<max and col== max-1:
            return printStar(row+1, 0, list, 2)
        else:
            return printStar(row, col+1, list, 1)        
    else:
        return

printStar(0, 0, list, 1)
for i in list:
    for j in i:
        print(j, end="")
    print()
