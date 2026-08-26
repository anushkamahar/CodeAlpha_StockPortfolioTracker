stock_prices ={
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "AMZN": 190,
    "MSFT": 420,
}
portfolio = []
total_investment = 0

while True:
    stock = input("enter stock name :").upper()

    if stock in stock_prices:
        print("Stock available")

        quantity = int(input("enter quantity :"))
        price = stock_prices[stock]
        investment = price*quantity
        total_investment += investment
        portfolio.append(f"{stock} : {quantity} x {price} = {investment}")
        print(f"{stock} : {quantity} x {price} = {investment}")
    else:
        print("Stock not available!")
    while True:
        choice = input("Do you want to add another stock? (yes/no): ").lower()
    
        if choice == "yes":
            break
        elif choice == "no":
            break
        else:
            print("please enter only yes or no.")
    
    if choice == "no":
        break

print("Total investment :",total_investment)

with open("portfolio.txt","w") as file:
    file.write("=====STOCK PORTFOLIO=====\n")
    for item in portfolio:
        file.write(item + "\n")
    file.write(f"\nTotal investment :{total_investment}\n")
                 



