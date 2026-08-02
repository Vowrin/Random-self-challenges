import csv
import os

CSV_PATH = os.path.join(os.path.dirname(__file__), 'produceSheets.csv')


def ensure_csv_exists():
    if not os.path.exists(CSV_PATH):
        with open(CSV_PATH, 'w', newline='') as csvfile:
            fieldnames = ['produce', 'quantity', 'price']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()


def new_produce(produce_name, quantity, price):
    ensure_csv_exists()
    with open(CSV_PATH, 'a', newline='') as csvfile:  # append without overwriting the existing file
        fieldnames = ['produce', 'quantity', 'price']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({'produce': produce_name.lower(), 'quantity': quantity, 'price': price})


def calculate_total_spending(produce_name, filename=CSV_PATH): #should be saved honestly, spending was meant as "possible spending but instead was saved"
    total_spending = 0.0
    with open(filename, 'r') as csvfile:
        data = csv.DictReader(csvfile)
        for row in data:
            if row['produce'] == produce_name.lower():
                total_spending += float(row['quantity']) * float(row['price'])
    return round(total_spending,2)

def calculate_total_gathered(produce_name,filename=CSV_PATH):
    total_quantity = 0
    with open(filename, 'r') as csvfile:
        data = csv.DictReader(csvfile)
        for row in data:
            if row['produce'] == produce_name.lower():
                total_quantity += float(row['quantity'])
    return total_quantity

#testing below
#print(calculate_total_spending('produce-sheets.csv', 'tomatoes'))  #expected 39 - PASSED before commending the code above and adding the function new_produce
#new_produce('tomatoes', 5, 2.0) #add more tomatoes to see if it calculates correctly
#print(calculate_total_spending('produce-sheets.csv', 'tomatoes'))  #expected 35 with the code from line 26 to 39 commented out - PASS
#print(calculate_total_gathered('produce-sheets.csv', 'tomatoes'))  #expected 15 with the code from line 26 to 39 commented out - PASS
