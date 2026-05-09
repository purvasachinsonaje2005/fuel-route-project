import openrouteservice
import folium

API_KEY = "eyJvcmciOiI1YjNjZTM1OTc4NTExMTAwMDFjZjYyNDgiLCJpZCI6ImMyZDhiNGQ0OWYzZTQ4YWVhOTg2Njc5YzZkYWY1OWUwIiwiaCI6Im11cm11cjY0In0="

client = openrouteservice.Client(key=API_KEY)


def get_route(start_coords, end_coords):

    route = client.directions(
        coordinates=[start_coords, end_coords],
        profile='driving-car',
        format='geojson'
    )

    return route


def generate_route_map(route_data):

    coordinates = route_data['features'][0]['geometry']['coordinates']

    # Convert longitude-latitude to latitude-longitude
    route_points = [(coord[1], coord[0]) for coord in coordinates]

    # Create map
    route_map = folium.Map(
        location=route_points[0],
        zoom_start=5
    )

    # Draw route
    folium.PolyLine(
        route_points,
        color="blue",
        weight=5
    ).add_to(route_map)

    # Start marker
    folium.Marker(
        route_points[0],
        tooltip="Start"
    ).add_to(route_map)

    # End marker
    folium.Marker(
        route_points[-1],
        tooltip="Finish"
    ).add_to(route_map)

    # Save map
    map_path = "maps/route_map.html"

    route_map.save(map_path)

    return map_path