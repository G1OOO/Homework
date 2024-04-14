book1 = 20
book2 = 15
book3 = 25
book4 = 30
book5 = 18
book6 = 22
book7 = 17
book8 = 28
book9 = 21
book10 = 35

total_price = book1 + book2 + book3 + book4 + book5 + book6 + book7 + book8 + book9 + book10
discount_5 = 0.1 * (book1 + book2 + book3 + book4 + book5)
discount_20 = 0.2 * (book6 + book7 + book8 + book9 + book10)

final_price = total_price - discount_5 - discount_20

print("Total Price:", total_price)
print("Discount for 5 Books (10%):", discount_5)
print("Discount for 5 Books (20%):", discount_20)
print("Final Price after Discounts:", final_price)
