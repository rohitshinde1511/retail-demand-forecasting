def calculate_reorder_quantity(
    forecast_demand,
    current_inventory,
    safety_stock=0
):
    """
    Simple reorder logic:
    Reorder = forecast + safety stock - current inventory
    """
    reorder_qty = forecast_demand + safety_stock - current_inventory
    return max(0, int(round(reorder_qty)))


def estimate_costs(
    forecast_demand,
    actual_demand,
    holding_cost_per_unit=2,
    stockout_cost_per_unit=10
):
    """
    Estimate cost impact based on forecast accuracy
    """
    if actual_demand > forecast_demand:
        stockout_units = actual_demand - forecast_demand
        return stockout_units * stockout_cost_per_unit
    else:
        excess_units = forecast_demand - actual_demand
        return excess_units * holding_cost_per_unit
