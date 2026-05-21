# Fuel Route Optimization API

## Overview

This project is a Django REST API that calculates optimized driving routes, estimates fuel costs, identifies fuel stops, and generates interactive route maps for logistics and transportation planning.

The application integrates external routing services and fuel pricing datasets to provide efficient route and fuel management.

---

## Features

- Route optimization between source and destination
- Distance calculation in miles
- Fuel cost estimation
- Fuel stop identification based on vehicle range
- Cheapest fuel station selection using CSV dataset
- Interactive route map generation using Folium
- REST API response in JSON format

---

## Technologies Used

- Python
- Django
- Django REST Framework
- Pandas
- Folium
- OpenRouteService API

---

## Project Structure

```bash
fuel_route_project/
│
├── manage.py
├── requirements.txt
├── README.md
├── fuel-prices-for-be-assessment.csv
│
├── maps/
│   └── route_map.html
│
├── fuel_route_project/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│
├── route_api/
│   ├── views.py
│   ├── urls.py
│   ├── services.py
│   ├── fuel_logic.py
```

---

## Installation

### Clone Repository

```bash
git clone <your-github-repo-link>
```

### Navigate to Project Folder

```bash
cd fuel_route_project
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Server

```bash
python manage.py runserver
```

Server runs at:

```text
http://127.0.0.1:8000/
```

---

## API Endpoint

### POST Request

```text
/api/route/
```

---

## Request Example

```json
{
    "start": "Chicago, IL",
    "finish": "Dallas, TX"
}
```

---

## Response Example

```json
{
    "start": "Chicago, IL",
    "finish": "Dallas, TX",
    "distance_miles": 967.01,
    "fuel_stops": [
        {
            "truckstop_name": "7-ELEVEN #218",
            "city": "Harrold",
            "state": "TX",
            "price_per_gallon": 2.68733333
        }
    ],
    "total_fuel_cost": 338.36,
    "map_file": "maps/route_map.html"
}
```

---

## Fuel Optimization Logic

- Vehicle mileage assumed: 10 miles per gallon
- Maximum vehicle range: 500 miles
- Fuel stops are selected using the lowest retail fuel prices from the dataset

---

## Map Generation

The project generates an interactive HTML route map using Folium.

Generated map file:

```text
maps/route_map.html
```

---

## Demonstration

The project demonstration includes:
- API testing using Thunder Client/Postman
- JSON response generation
- Interactive route visualization
- Fuel stop optimization workflow

---



## Output Screenshots

### API Response

<img width="900" alt="API Response" src="<img width="1917" height="932" alt="image" src="https://github.com/user-attachments/assets/86a85652-47e3-4043-aa62-f361076d7e67" />
">

---

### Generated Route Map

<img width="900" alt="Route Map" src="PASTE_ROUTE_MAP_SCREENSHOT_LINK_HERE">

---

## Conclusion

This project demonstrates backend API development using Django REST Framework with route optimization, fuel estimation, CSV-based fuel pricing analysis, and interactive route visualization.

## Author

Purva Sonaje
