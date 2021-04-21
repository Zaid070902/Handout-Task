def hotel_cost(nights):
    return 140 * nights


def plane_ride_cost(city):
    if "Cape_Town" == city:
        return 2500
    elif "Durban" == city:
        return 2300
    elif "JHB" == city:
        return 2000
    elif "BNF" == city:
        return 1800
    else:
        return "Location not in database"


def rent_car_cost(days):
    car_cost = 40 * days

    if days >= 7:
        car_cost = car_cost - 50
    elif days >= 3 and days <= 7:
        car_cost = car_cost - 20
    return car_cost


def trip_cost(city, days, spending_money):
    return rent_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money


print(trip_cost("JHB", 7, 100))
