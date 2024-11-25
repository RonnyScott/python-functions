def calculate_discount(price, discount_percent):
   
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price


try:
    price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))

    final_price = calculate_discount(price, discount_percent)

    if final_price != price:
        print(f"The final price after applying the discount is: Ksh.{final_price:.2f}")
    else:
        print(f"No discount applied. The original price is: Ksh.{price:.2f}")
except ValueError:
    print("Please enter valid numeric values for price and discount.")