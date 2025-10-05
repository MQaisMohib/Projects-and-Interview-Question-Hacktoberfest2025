def apply_discount(price, discount_percent):
    discount = (price * discount_percent) / 100
    return price - discount

price = float(input("Enter product price: "))
discount = float(input("Enter discount percentage: "))
print("Final price after discount =", apply_discount(price, discount))
