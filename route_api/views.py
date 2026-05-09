from rest_framework.views import APIView
from rest_framework.response import Response

from geopy.geocoders import Nominatim

from .services import get_route, generate_route_map
from .fuel_logic import calculate_fuel_cost, get_fuel_stops


class RouteView(APIView):

    def post(self, request):

        start_city = request.data.get("start")
        finish_city = request.data.get("finish")

        geolocator = Nominatim(user_agent="fuel_app")

        start_location = geolocator.geocode(start_city)
        finish_location = geolocator.geocode(finish_city)

        start_coords = [
            start_location.longitude,
            start_location.latitude
        ]

        finish_coords = [
            finish_location.longitude,
            finish_location.latitude
        ]

        # Get route
        route_data = get_route(start_coords, finish_coords)

        # Generate map
        map_path = generate_route_map(route_data)

        # Distance calculation
        distance_meters = route_data['features'][0]['properties']['segments'][0]['distance']

        distance_miles = distance_meters * 0.000621371

        # Fuel calculations
        total_cost = calculate_fuel_cost(distance_miles)

        fuel_stops = get_fuel_stops(distance_miles)

        return Response({
            "start": start_city,
            "finish": finish_city,
            "distance_miles": round(distance_miles, 2),
            "fuel_stops": fuel_stops,
            "total_fuel_cost": total_cost,
            "map_file": map_path
        })