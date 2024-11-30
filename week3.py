def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        return price - (price * discount_percent / 100)
    else:
        return price

def main():
    try:
        price = float(input("Enter the original price: "))
        discount_percent = float(input("Enter the discount percentage: "))
        final_price = calculate_discount(price, discount_percent)
        if final_price == price:
            print("No discount applied. The original price is:", price)
        else:
            print("The final price after applying the discount is:", final_price)
    except ValueError:
        print("Please enter valid numerical values for price and discount percentage.")

if __name__ == "__main__":
    main()
