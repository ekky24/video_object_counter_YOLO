from shapely.geometry import Polygon

LOCATION_CONF = {
    'sol': {
        'host': '103.167.31.202:554/H.264',
        'username': 'admin',
        'password': 'KGMJLP',
        'area': 'sol',
        'max_capacity': [10],
        'region': [
            {
                "name": "sol_1",
                "polygon": Polygon([(21, 80), (21, 665), (1240, 665), (1240, 80)]),  # Polygon points
                "counts": 0,
                "draggin": False,
                "region_color": (37, 255, 255), # BGR value
                "text_color": (0, 0, 0) # Region text color
            },
            # {
            #     "name": "sol_2",
            #     "polygon": Polygon([(460, 100), (600, 100), (665, 458), (417, 557)]),  # Polygon points
            #     "counts": 0,
            #     "draggin": False,
            #     "region_color": (37, 255, 255), # BGR value
            #     "text_color": (0, 0, 0) # Region text color
            # }
        ]
    }
}