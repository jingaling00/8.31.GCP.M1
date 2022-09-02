# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 13:24:02 2022

@author: jingy
"""
# calculate net pay with hours worked
# by Jingyan Zhang
hours = float(input("Hours worked: ")) 
pay_rate = float(input("Pay rate: "))
pay = pay_rate * hours # gross pay
tax_perc = 0.16
parking = 3.5
net_pay = (1-tax)*(pay-parking) 
print("Gross weekly pay: " + str(pay))
print("Net weekly pay: " + str(round(net_pay,2)))

# calculate wholesale price of books ordered
# by Jingyan Zhang
numCopies = int(input('Number of book copies: '))
book = 30.92
discount = 0.65
book_price = book*discount
first_book = book_price + 3 # price of first book with shipping
remain_books = (numCopies-1)*(book_price+0.75) # price of remaining books with shipping
wholesale_price = first_book + remain_books
print("Wholesale price: " + str(round(wholesale_price, 2)))



