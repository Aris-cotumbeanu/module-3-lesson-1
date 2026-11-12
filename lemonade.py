def greet_customer():   
    print ("Welcome to the lemonade shop!")
    print ("Fresh lemonade, made for you!")

greet_customer()

price_per_cup = float(input("Enter the price per cup in pounds: "))
cups_sold = int(input("Enter the number of cups sold: "))

def calculate_total(price, cups):
    total = price * cups
    return total

total_cost = calculate_total(price_per_cup, cups_sold)

rounded_total = round(total_cost, 2)
print("total cost: ", rounded_total)

amount_paid = float(input("Enter the amount paid by the customer in pounds: "))

def calculate_change(paid, total):
    change = paid - total
    return change

change_due = calculate_change(amount_paid, rounded_total)
rounded_change = round(change_due, 2)
print("change due: ", rounded_change)
def thank_you_message(cups):
    if cups > 5:
        return"thanks for such a big order!"
    else:
        return"thanks for stopping by the shop!"

closing_message = thank_you_message(cups_sold)

print("")
print("=====Lemonade shop receipt=====")
print("price per cup:", price_per_cup)
print("number of cups sold:", cups_sold)
print("total cost:", rounded_total)
print("amount paid:", amount_paid)
print("change due:", rounded_change)
print("closing message:", closing_message)
print("================================")