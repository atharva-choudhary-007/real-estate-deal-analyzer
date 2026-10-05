def calculate_deal(
    purchase_price,
    arv,
    rehab_cost,
    closing_costs,
    holding_costs,
    assignment_fee,
    target_roi
):
    total_cost = (
        purchase_price
        + rehab_cost
        + closing_costs
        + holding_costs
        + assignment_fee
    )

    profit = arv - total_cost
    roi = (profit / total_cost) * 100

    target_total_cost = arv / (1 + target_roi / 100)

    max_purchase_price = (
        target_total_cost
        - rehab_cost
        - closing_costs
        - holding_costs
        - assignment_fee
    )

    if profit > 0 and roi >= target_roi:
        rating = "MEETS TARGET"
    elif profit > 0:
        rating = "BELOW TARGET"
    else:
        rating = "LOSS"

    return {
        "total_cost": total_cost,
        "profit": profit,
        "roi": roi,
        "max_purchase_price": max_purchase_price,
        "rating": rating
    }
