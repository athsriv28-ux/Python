status = input("Enter your current membership status: ")
price = float(input("Enter the price of the item(s) you purchased($):  "))

if status == "gold" or status == "Gold":
  print("\nMembership Status: Gold")
  if price >= 10000:
    print("Price of item(s) purchased: $", price)
    print("Discount given: 20%")
    final = float(print("Discounted price: $", price * (20/100)))
  elif price < 10000:
    print("Price of item(s) purchased: $", price)
    print("Discount given: 10%")
    final = float(print("Discounted price: $", price * (10/100)))
  else:
    print("Invalid input. Please try again.")
elif status == "silver" or status == "Silver":
  print("\n< Membership Discount Calculator >")
  print("\nMembership Status: Silver")
  if price >= 10000:
    print("Price of item(s) purchased: $", price)
    print("Discount given: 15%")
    final = float(print("Discounted price: $", price * (15/100)))
  elif price < 10000:
    print("Price of item(s) purchased: $", price)
    print("Discount given: 10%")
    final = float(print("Discounted price: $", price * (10/100)))
  else:
    print("Invalid input. Please try again.")
elif status == "regular" or status == "Regular":
   print("\n< Membership Discount Calculator >")
   print("\nMembership Status: Regular")
   if price >= 10000:
    print("Price of item(s) purchased: $", price)
    print("Discount given: 5%")
    final = float(print("Discounted price: $", price * (5/100)))
   elif price < 10000:
    print("Price of item(s) purchased: $", price)
    print("Discount given: 0%")
    final = float(print("Discounted price: $", price))
   else:
    print("Invalid input. Please try again.")
else:
 print("Invalid input please try again.")

if price >= 2000:
  delivery = float(0)
  print("\nDelivery charge: $", delivery)
  print("Final price: $", final )
  print("\nEnjoy your shopping!")
  print("Please come again!")
elif price < 2000:
  delivery = float(100)
  print("\nDelivery charge: $", delivery)
  print("Final price: $", final + delivery)
  print("\nEnjoy your shopping!")
  print("Please come again!")

