""" Stock Protfolio Tracker 
Goal:- Build a simple stock tracker that calculate total investment based on manually defined stock prices"""
import pandas as pd 
print("|=======================================|")
print("|        Stock Protfolio Tracker        |")
print("|=======================================|\n")
Stock_Price={"AAPL":180,"TSLA":250,"GOOG":130,"MSFT":310,"AMZN":145}
print("Stock_Price:",Stock_Price.items())
total_value=0
protfolio=[]
stock_name=""
while True:
    stock_name=input("Enter a Stock name:")
    print("type done to end program")
    if stock_name.lower()=="done":
        break
    stock_name=stock_name.upper()
    if stock_name not in Stock_Price:
        print("Stock not found")
        continue
    quantity=int(input("enter a quantity:"))
    price = Stock_Price[stock_name]
    value = price * quantity
    print("value:\n", value)
    protfolio.append((stock_name,quantity,value ))
    print("protfolio: \n ",protfolio)
    total_value += value 
print("\nFinal Portfolio:", protfolio)
print("Total Portfolio Value:", total_value)
csv_01=pd.DataFrame(protfolio,columns=["Stock","Quantity","Value"])
row = pd.DataFrame([["TOTAL","", total_value]], columns=["Stock","Quantity","Value"])
csv_01 = pd.concat([csv_01,row])
csv_01.to_csv("protfolio.csv",index=False)
print("Saved successfully")


