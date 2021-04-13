# Function for nth Fibonacci number
def Fibonacci(n):
   
    # Check if input is 0 then it will
    # print incorrect input
    if n < 0:
        print("Incorrect input")
 
    # Check if n is 0
    # then it will return 0
    elif n == 0:
        return 0
 
    # Check if n is 1,2
    # it will return 1
    elif n == 1 or n == 2:
        return 1
 
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)



def factorial(n):
    facto=1
    if n<0:
        return "Sorry, factorial does not exist for negative numbers"
    elif n == 0:
        return "The factorial of 0 is 1"
    else:
        for i in range(1,n + 1):
            facto = facto*i
        return facto
       