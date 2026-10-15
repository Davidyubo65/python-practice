# 1. Input the prices of four products
usb_price = float(input("Please enter the price of the USB drive: "))
tf_card_price = float(input("Please enter the price of the TF card: "))
drink_price = float(input("Please enter the price of the beverage: "))
cable_price = float(input("Please enter the price of the network cable: "))

# 2. Calculate the total amount
total = usb_price + tf_card_price + drink_price + cable_price

# 3. Print the shopping receipt
print("\n" + "=" * 48)
print("                 SHOPPING RECEIPT")
print("=" * 48)

print(f"{'Product':<22}{'Qty':>5}{'Price':>10}{'Amount':>11}")
print("-" * 48)

print(f"{'Kingston USB 8GB':<22}{1:>5}{usb_price:>10.2f}{usb_price:>11.2f}")
print(f"{'16GB TF Card':<22}{1:>5}{tf_card_price:>10.2f}{tf_card_price:>11.2f}")
print(f"{'Beverage':<22}{1:>5}{drink_price:>10.2f}{drink_price:>11.2f}")
print(f"{'Network Cable 2m':<22}{1:>5}{cable_price:>10.2f}{cable_price:>11.2f}")

print("-" * 48)
print(f"Total quantity: 4       Total amount: {total:.2f}")
print(f"Amount due: {total:.2f}")
print(f"Amount received: {total:.2f}")
print(f"Change: 0.00")
print("=" * 48)
git push

