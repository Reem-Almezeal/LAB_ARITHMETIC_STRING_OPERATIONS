print("Welcome in Arithmetic Operations System\n")

Price=2.99
Quantity=3
tax_rate=0.075 *100


SubTotal=Price*Quantity
Tax=SubTotal*tax_rate
TotalCost=SubTotal+Tax


print("Price of item : ",Price," $")
print("Quantity : ",Quantity)
print("Tax Rate : ",tax_rate ," %\n")

print("Sub Total : ",SubTotal," $")
print("Tax : ",round(Tax,2)," $")
print("Total Cost : ",round(TotalCost,2)," $")

