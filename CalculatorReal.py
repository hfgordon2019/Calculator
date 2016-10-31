from Myro import *
print("welcome to the calculator program!")
#Addition

def add(num1, num2):
    result = num1;
    for i in range(0,num2):
      #  print(i)
        result = result +1
    return result
    
answer = add(5,5)    
print(answer)

#Subtraction

def sub(num1, num2):
    result = num1;
    for i in range(0,num2):
        #print(i)
        result = result -1
    return result
    
answer = sub(18,15)    
print(answer)

#Multiplication

def multiply(num1, num2):
    result = 0;
    for i in range(num2):
      #  print(i)
        result = add(result,num1);
    return result
  #  add result to num1 num2 times
answer = multiply(10,5)    
print(answer)

#Division
def divide(num1,num2):
    result = 0
    while num1>0:
        num1 = sub(num1,num2);
        result = result +1 
    if num1<0 :
        result = result -1
    print (num1) 
    return result 
answer = divide (18,7)
print(answer)



