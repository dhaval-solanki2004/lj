# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 19:10:00 2026

@author: dhava
"""

unit=int(input("enter number of unit:"))
fix_charge=50
bill=0

if unit<=50:
   bill=unit*3.30+fix_charge
   
elif unit>=51 and unit<=200:
    bill=unit*3.95+fix_charge
    
else:    
    bill=unit*5.00+fix_charge   


print("Your Total Bill=rs",bill)