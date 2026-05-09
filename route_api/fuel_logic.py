import pandas as pd

# Load CSV
df = pd.read_csv("fuel-prices-for-be-assessment.csv")

# Clean column names
df.columns = df.columns.str.strip()


def calculate_fuel_cost(distance_miles):

    gallons_needed = distance_miles / 10

    avg_price = df['Retail Price'].mean()

    total_cost = gallons_needed * avg_price

    return round(total_cost, 2)


def get_fuel_stops(distance_miles):

    fuel_stops = []

    max_range = 500

    stops_needed = int(distance_miles // max_range)

    # Find cheapest fuel station
    cheapest_station = df.nsmallest(1, 'Retail Price')

    for i in range(stops_needed):

        fuel_stops.append({
            "truckstop_name": str(cheapest_station.iloc[0]['Truckstop Name']),
            "city": str(cheapest_station.iloc[0]['City']),
            "state": str(cheapest_station.iloc[0]['State']),
            "price_per_gallon": float(cheapest_station.iloc[0]['Retail Price'])
        })

    return fuel_stops