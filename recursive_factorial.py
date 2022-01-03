n= int(input())

def factorial(num):
    if num<= 1:
        return 1
    return n* factorial(num-1)

print(factorial(n))
