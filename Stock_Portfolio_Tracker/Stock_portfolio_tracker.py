stocks = {
    "APPL": 180,
    "TSLA": 250,
    "GOOG": 150

}

stock_name = input("Please Enter Stock Name:").upper()
quantity = int(input("Enter Quantity"))

if stock_name in stocks:
    total = stocks[stock_name]*quantity

    print("\n****Stock Details****")
    print("Stock Name:",stock_name)
    print("Price :", stocks[stock_name])
    print("Quantity :", quantity)
    print("Total Value:" , total)

    file = open("stock_result.txt", "w")
    file.write("stock name:" + stock_name + "\n")
    file.write("Price:" + str(stocks[stock_name]) + "\n")
    file.write("Quantity:" + str(quantity) + "\n")
    file.write("Total Investment :"+ str(total))
    file.close()

    print("\nResult saved in stock_result.txt")

else:
    print("Try Again! Stock not Found!")
