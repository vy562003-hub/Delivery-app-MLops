"Is this order usable?"


def is_valid_order(order):
    if (order["distance_km"] > 0 and order["prep_time_min"] >= 0 and order["traffic_level"] in [1,2,3] and order["rain"] in [0,1]):
        return True

    return False
