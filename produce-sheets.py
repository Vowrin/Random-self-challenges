import csv

data = [
    {'produce': 'tomatoes', 'quantity': 10, 'price': 2.5},
    {'produce': 'potatoes', 'quantity': 5, 'price': 1.5},
    {'produce': 'carrots', 'quantity': 8, 'price': 1.0},
    {'produce': 'peppers', 'quantity': 3, 'price': 1.2},
]


with open('produce-sheets.csv', 'w', newline='') as csvfile: #w for write
    fieldnames = ['produce', 'quantity', 'price']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for item in data:
        writer.writerow(item)
#so far we've written in the file with already existing data. Next goal is to add to that
def new_produce(produce_name, quantity, price):
    with open('produce-sheets.csv', 'a', newline='') as csvfile: #a for append as we dont want to overwrite the existing data
        fieldnames = ['produce', 'quantity', 'price']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({'produce': produce_name, 'quantity': quantity, 'price': price})

#------------------------------------------------ 1st attempt at adding more data to the csv file. This works but the goal is for reusable code
#with open('produce-sheets.csv', 'a', newline='') as csvfile: #a for append as we dont want to overwrite the existing data
#   fieldnames = ['produce', 'quantity', 'price']
#    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # New data to append
#    new_data = [
#        {'produce': 'cucumbers', 'quantity': 6, 'price': 1.8},
#        {'produce': 'lettuce', 'quantity': 4, 'price': 1.5},
#        {'produce': 'tomatoes', 'quantity': 7, 'price': 2.0}, #repeat item to see if it appends correctly
#    ]

#    for item in new_data:
#        writer.writerow(item)
#works so far. Now we want to extract "total spending"  --------------------------- old code above

def calculate_total_spending(filename, produce_name):
    total_spending = 0.0
    with open(filename, 'r') as csvfile:
        data = csv.DictReader(csvfile)
        for row in data:
            if row['produce'] == produce_name:
                total_spending += int(row['quantity']) * float(row['price'])
    return total_spending

def calculate_total_gathered(filename, produce_name):
    total_quantity = 0
    with open(filename, 'r') as csvfile:
        data = csv.DictReader(csvfile)
        for row in data:
            if row['produce'] == produce_name:
                total_quantity += int(row['quantity'])
    return total_quantity

print(calculate_total_spending('produce-sheets.csv', 'tomatoes'))  #expected 39 - PASSED before commending the code above and adding the function new_produce
new_produce('tomatoes', 5, 2.0) #add more tomatoes to see if it calculates correctly
print(calculate_total_spending('produce-sheets.csv', 'tomatoes'))  #expected 35 with the code from line 26 to 39 commented out - PASS
print(calculate_total_gathered('produce-sheets.csv', 'tomatoes'))  #expected 15 with the code from line 26 to 39 commented out - PASS
