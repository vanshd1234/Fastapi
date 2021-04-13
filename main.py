#import libraries for creating api
from fastapi import FastAPI
import math1 # this is math module 
import string1 # string module 

app= FastAPI()
# home page 
@app.get('/')
def index():
    return 'Hello to check Module info check localhost:8000/docs'



# this is to find fabonacci series sum by given nth no of value
@app.get('/facbonacci')
def fab(number:int):
    fabo=math1.Fibonacci(number)
    return fabo

# to find the factorial of any number but not the negative value
@app.get('/factorial')
def fac(number:int):
    fac=math1.factorial(number)
    return fac

# To find the string length which user want to enter     
@app.get('/string length')
def str(string:str):
    length=string1.lenthst(string)
    return length

# creete a string from custom character and given length
@app.get('/generate string')
def gen(w,q):
    set1=list(w)
    k=int(q)
    return string1.setlength(set1,k)
    

