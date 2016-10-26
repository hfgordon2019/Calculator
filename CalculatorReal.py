from Myro import *

#Addition

def add(num1, num2):
    result = num1;
    for i in range(0,num2):
        print(i)
        result = result +1
    return result
    
answer = add(5,5)    
#print(answer)

#Subtraction

def sub(num1, num2):
    result = num1;
    for i in range(0,num2):
        #print(i)
        result = result -1
    return result
    
answer = sub(18,15)    
#print(answer)

#Multiplication

def multiply(num1, num2):
    result = 0;
    for i in range(num2):
        print(i)
        result = add(result,num1);
    return result
  #  add result to num1 num2 times
answer = multiply(10,5)    
print(answer)
