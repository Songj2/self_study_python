n= int(input())
list=[["*" for j in range(n)] for i in range(n)]

def printStar(row, col, list, way):
    max= len(list)    
    temp= 3
    if row<max and col<max:
        while temp<= max:
            print("temp/3: ", temp/3, "row: ", row, "col:", col, "temp/3*2: ", (temp/3)*2)
            if temp/3<=row<(temp/3)*2 and temp/3<=col<(temp/3)*2:
                list[row][col]= " "
                
            elif way== 1:
                if temp/3<=col<(temp/3)*2 and col%3==1 and row%3==1: #and row조건
                    list[row][col]= " "
                    print("COLUMN")
            elif way== 2:
                if temp/3<=row<(temp/3)*2 and row% 3==1 and col%3 == 1 : #and col조건
                    list[row][col]= " "
                    print("ROW")
    
            temp*=3 
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
