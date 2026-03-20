price = 24.95
discount_price = price * 0.6

total_books = 60

book_cost = discount_price * total_books
shipping = 3 + (total_books - 1) * 0.75

total = book_cost + shipping

print("Tổng chi phí:", total)