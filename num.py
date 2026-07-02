# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 19:17:29 2026

@author: dhava
"""

ch=0
while True:
    print("-------------------------------------------")
    print("1.Binary convert")
    print("2.Octal convert")
    print("3.HexaDecimal convert")
    print("0.Exit")
    ch=int(input("Enter Your choice:"))
    
    if ch==1:
        n=int(input("Enter Number for convert Into Binary"))
        print("Nuber converted done And Binary Number Is=",bin(n))
    elif ch==2:
        n=int(input("Enter Number for convert Into Octal"))
        print("Nuber converted done And Binary Number Is=",oct(n))    
    elif ch==3:
        n=int(input("Enter Number for convert Into Octal"))
        print("Nuber converted done And Binary Number Is=",hex(n))    
    elif ch==0:
        break
    else:
        print("Enteer valid choice!!!! ")
    
    pass