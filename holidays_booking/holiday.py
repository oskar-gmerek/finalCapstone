############## *** T16 *** ###################
# The 16th task in HyperionDev Bootcamp.
# Student registration form
##############################################

# Usable constants
SACRAMENTO = 'Sacramento'
ZAKOPANE = 'Zakopane'
EASTBOURNE = 'Eastbourne'
GDANSK = 'Gdańsk'
DESTINATIONS = [SACRAMENTO, ZAKOPANE, EASTBOURNE, GDANSK, 'Gdansk']

rebate = 0
promo_code = ''


def hotel_cost(city_flight: str, num_nights: int):
    """ Hotel cost calculation function

    Args:
        city_flight (str): Name of the destination city
        num_nights (int): Number of nights

    Raises:
        ValueError: Unexpected error handler (wrong city_flight)

    Returns:
        float: Price of hotel stay
    """
    if city_flight == SACRAMENTO:
        night_cost = 366.00
        full_hotel_cost = night_cost * num_nights
    elif city_flight == ZAKOPANE:
        night_cost = 319.00
        full_hotel_cost = night_cost * num_nights
    elif city_flight == EASTBOURNE:
        night_cost = 276.00
        full_hotel_cost = night_cost * num_nights
    elif city_flight in [GDANSK, 'Gdansk']:
        night_cost = 224.00
        full_hotel_cost = night_cost * num_nights
    else:
        # This should never happen
        raise ValueError("Wrong destination")
    return round(full_hotel_cost, 2)


def plane_cost(city_flight: str):
    """ Flight cost calculation function

    Args:
        city_flight (str): Name of the destination city

    Raises:
        ValueError: Unexpected error handler (wrong city_flight)

    Returns:
        float: Price of the flight
    """
    if city_flight == SACRAMENTO:
        price = 428.00
    elif city_flight == ZAKOPANE:
        price = 113.00
    elif city_flight == EASTBOURNE:
        price = 286.00
    elif city_flight in [GDANSK, 'Gdansk']:
        price = 92.00
    else:
        # This should never happen
        raise ValueError("Wrong destination")
    return round(price, 2)


def car_rental(rental_days: int):
    """ Car rental calculation function

    Args:
        rental_days (int): Number of rental days

    Returns:
        float: Cost of car rental
    """
    dayrate = 323.98
    car_cost = dayrate * rental_days
    return round(car_cost, 2)


def holiday_cost(hotel_cost: float, plane_cost: float, car_rental: float):
    """ Holiday cost calculation function

    Args:
        hotel_cost (float): Price of hotel stay
        plane_cost (float): Price of flight
        car_rental (float): Price of car rental

    Returns:
        float: Full cost of holidays
    """
    full_cost = hotel_cost + plane_cost + car_rental
    return round(full_cost, 2)


def discounted_cost(holiday_cost: float, rebate: float):
    """ Discount calculation function

    Args:
        holiday_cost (float): Base amount to discount
        rebate (float): Amount of discount in percentage 

    Returns:
        float: Amount after the discount
    """
    discounted = holiday_cost * (1 - rebate/100)
    return round(discounted, 2)


def plural(count):
    """ Pluralization function to preserve grammatically correct suffixes.

    Args:
        count (int): Plural Count

    Returns:
        str: 's' or ''
    """
    if count == 1:
        return ''
    else:
        return 's'


print('''
**********************************************************************************
                Dreamdays Holidays - Book your dream holidays
**********************************************************************************
=============================== ❗DISCOUNT OFFER❗ ===============================
Escape to the beautiful city of Gdańsk, located by the stunning Baltic Sea! 
Our 7-day holiday package offers you the chance to explore the city's 
rich history and culture, indulge in delicious Polish cuisine, 
and enjoy the refreshing sea breeze.

30% OFF Promo Code: PolandSea23

----------------------------------------------------------------------------------
🟢 Available destinations: 'Sacramento', 'Zakopane', 'Eastbourne' and 'Gdańsk'
----------------------------------------------------------------------------------
''')

while True:
    try:
        # Get input data from the user
        promo = str(input("Do you want to use promo code? (y/n): "))
        if promo == 'y':
            promo_code = str(input("Enter promo code: "))
            if promo_code == "PolandSea23":
                city_flight = GDANSK
                num_nights = 7
                rental_days = int(
                    input(f"Number of days you will need a car (0-{num_nights}): "))
                rebate = 30
            else:
                print("❌ This is not a valid promo code or is expired. \n")
                continue
        elif promo == 'n':
            print(
                "🟠 The Promo code wasn't applied. You chose our regular, but a still great offer. \n")
            city_flight = str(
                input("Enter city you like to visit: ")).capitalize()

            if city_flight not in DESTINATIONS:
                print(
                    f'''
            Oh, so sorry! {city_flight} destination is not available yet.
            Currently available destinations are: {SACRAMENTO}, {ZAKOPANE}, {EASTBOURNE} and {GDANSK}
                    ''')
                continue

            num_nights = int(
                input("Enter number of nights you want to stay (1-21): "))
            if num_nights < 1:
                raise ZeroDivisionError
            elif num_nights > 21:
                print("❌ We currently do not offer holidays longer than 21 days. \n")
                continue
            rental_days = int(
                input(f"Number of days you will need a car (0-{num_nights}): "))

            if rental_days > num_nights:
                print(
                    f"❌ You can't rent a car for longer than {num_nights} because you have to return it before your flight home. \n ")
                continue
        else:
            continue

        # Use functions to calculate costs
        hotel_price = hotel_cost(city_flight, num_nights)
        flight_price = plane_cost(city_flight)
        car_price = car_rental(rental_days)
        full_cost = holiday_cost(hotel_price, flight_price, car_price)

        # Print confirmation details in the nice and readable way
        print(f'''
    ========== Your dream holidays are booked ============

        Destination: {city_flight}
        Flight: £{flight_price}
        Hotel****: {num_nights} night{plural(num_nights)} (£{hotel_price/num_nights} per night)
        Premium Car rental: {f" {rental_days} day{plural(rental_days)} (£{car_price/rental_days} per day)" if rental_days > 0 else 'Not included'} 
        

        TOTAL PRICE: £{full_cost} ''')
        if rebate <= 0:
            print('''
    ======================================================

        Thanks for choosing Dreamdays Holidays! 

    ======================================================
    ''')

        if rebate != 0:
            final_price = discounted_cost(full_cost, rebate)
            print(f'''
    ================ ✅ DISCOUNT APPLIED ================= 

        Promo code used: {promo_code}
        Rebate: -{rebate}% (£{round(full_cost-final_price, 2)})

        FINAL PRICE: £{final_price}

    ======================================================

        Thanks for choosing Dreamdays Holidays!     

    ======================================================
            ''')
        exit()

    # Catch errors
    except ZeroDivisionError:
        print(
            "❌ The input number must not be less than one. Let's start from the beginning. \n")
    except ValueError:
        print("❌ You have entered an invalid value. Let's start from the beginning. \n")

    # Catch unexpected errors
    except Exception as e:
        print(f'❌ Error: {e} \n')
