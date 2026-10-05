from calculator import calculate_deal


def get_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Please enter a positive number.")
                continue
            return value
        except ValueError:
            print("Please enter a valid number.")


print("=" * 45)
print("       REAL ESTATE DEAL ANALYZER")
print("=" * 45)

print("\nEnter the deal details:\n")

purchase_price = get_number("Purchase price ($): ")
arv = get_number("After Repair Value - ARV ($): ")
rehab_cost = get_number("Rehabilitation cost ($): ")
closing_costs = get_number("Closing costs ($): ")
holding_costs = get_number("Holding costs ($): ")
assignment_fee = get_number("Assignment fee ($): ")
target_roi = get_number("Target ROI (%): ")

result = calculate_deal(
    purchase_price,
    arv,
    rehab_cost,
    closing_costs,
    holding_costs,
    assignment_fee,
    target_roi
)

print("\n" + "=" * 45)
print("             DEAL ANALYSIS")
print("=" * 45)

print(f"Total cost:            ${result['total_cost']:,.2f}")
print(f"Expected profit:       ${result['profit']:,.2f}")
print(f"ROI:                   {result['roi']:.2f}%")
print(f"Max purchase price:    ${result['max_purchase_price']:,.2f}")
print(f"Deal assessment:       {result['rating']}")

print("=" * 45)
