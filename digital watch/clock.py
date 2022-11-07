# desine a simple clock on python ;
import time 

print('hi , we have create a clock : ')
n= int(input('enter the local  hour : '))
m= int(input('enter the local  minute  : '))
o= int(input('enter the local  secound : '))

def display():
    print(n , ':' , m , ':', o, ':')

def add():
    global n 
    global m 
    global o 
    o+=1 
    if o==60 :
        m+=1 
        o=0 
    if m==60:
        n+=1
        m=0 
    if o==24 :
        h=0 
    print('/n')
while True:
    time.sleep(1)
    display()
    add()
    
    