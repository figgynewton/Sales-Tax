Python 3.8.5 (v3.8.5:580fbb018f, Jul 20 2020, 12:11:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> amount = float(input("Please enter the amount of the purchase: $ "))
Please enter the amount of the purchase: $ 8.90
>>> state_tax = amount * 0.05
>>> county_tax = amount * 0.025
>>> total_tax = state_tax + county_tax
>>> sales_total = amount + total_tax
>>> print("State sales tax: $", format(state_tax, '.2f'), sep = "" )
State sales tax: $0.45
>>> print("County sales tax: $", format(county_tax, '.2f'), sep = "" )
County sales tax: $0.22
>>> print("Total sales tax: $", format(total_tax, '.2f'), sep = "" )
Total sales tax: $0.67
>>> print("Total: $", format(sales_tax, '.2f'), sep = "" )
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    print("Total: $", format(sales_tax, '.2f'), sep = "" )
NameError: name 'sales_tax' is not defined
>>> print("Total: $", format(sales_total, '.2f'), sep = "" )
Total: $9.57
>>> 