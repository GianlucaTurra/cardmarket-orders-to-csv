import scraper
import csv

data = scraper.get_order_library()

# Declare the csv file headings
orders_info = ['Card', 'Seller', 'Amount', 'Unit Prize']

with open('Order.csv', 'w', newline='') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=orders_info)
    writer.writeheader()
    writer.writerows(data)
