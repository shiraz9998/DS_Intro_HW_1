# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 18:35:58 2022

@author: WIN10
"""
#A
def my_fun(x1, x2, x3):
    mone=((x1+x2+x3)*(x2+x3)*x3)
    denomin = x1+x2+x3
    x= mone/denomin
    
    if denomin==0:
        return "Not a number – denominator equals zero"
                
    elif type(x1)==float and type(x2)==float and type(x3)==float:
        return x
    else:
        return "Error: parameters should be float"
    
print(my_fun(2,5,7))

#B
def convert(hours, minutes):
    if  hours>0 and minutes>0:
        
        hours_seconds= hours*60*60
        minutes_seconds= minutes*60
        sum_minutes= hours_seconds+minutes_seconds
        return sum_minutes
    
    else:
        return "Input error!"
    
print(convert(1.5,3))

