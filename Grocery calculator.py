# Step 1: Define the price list (item: price)
prices = {
    "apple": 20,
    "banana": 10,
    "milk": 40,
    "bread": 20,
    "eggs": 30
}

# Step 2: Define the purchase list (item: quantity)
# For beginners, we'll start with a pre-defined purchase
purchased_items = {
    "apple": 4,
    "milk": 2,
    "bread": 1
}

# Step 3: Compute the total bill
total_bill = 0

print("--- Your Receipt ---")

# We loop through the items actually purchased
for item, quantity in purchased_items.items():
    # Check if the purchased item exists in our price list
    if item in prices:
        price_per_unit = prices[item]
        item_total = price_per_unit * quantity
        total_bill += item_total
        
        print(f"{item.capitalize()}: {quantity} x {price_per_unit:}Rs = {item_total:}")
    else:
        print(f"Warning: {item} is not in the price list.")

print("-" * 20)
print(f"Grand Total: {total_bill:}Rs.")
