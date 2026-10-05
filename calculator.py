def calculate_deal(purchase_price, arv, rehab_cost, closing_costs, holding_costs, assignment_fee):
    total_cost = (
        purchase_price
        + rehab_cost
        + closing_costs
        + holding_costs
        + assignment_fee
    )

    profit = arv - total_cost
    roi = (profit / total_cost) * 100

    max_offer = (
        arv
        - rehab_cost
        - closing_costs
        - holding_costs
        - assignment_fee
    )

    if profit > 0 and roi >= 15:
        rating = "GOOD DEAL"
    elif profit > 0:
        rating = "MARGINAL DEAL"
    else:
        rating = "BAD DEAL"

    return {
        "total_cost": total_cost,
        "profit": profit,
        "roi": roi,
        "max_offer": max_offer,
        "rating": rating
    }
