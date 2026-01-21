
#if price in ILS add 18% TAX
#if price in $ add 20% TAX
prices = ["25$", "100EURO", "50$", "48ILS", "34$", "100ILS"]
ILS_prices = []
dollar_prices = []

for price in prices:
    if "ILS" in price:
        price = price.replace("ILS", "")
        price = int(price)*1.18
        ILS_prices.append(price)
    elif "$" in price:
        price = price.replace("$", "")
        price = int(price)*1.2
        dollar_prices.append(price)
    else:
        print(f"{price} is in invalid currency")

print(f"The prices in ILS are: {ILS_prices}")
print(f"The prices in dollars are: {dollar_prices}")

print("test end")