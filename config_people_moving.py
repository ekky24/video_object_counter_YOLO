from shapely.geometry import Polygon

LOCATION_CONF = {
    'mcd': {
        'host': '182.0.21.152:554/ch1/main',
        'username': 'admin',
        'password': 'IMGTDW',
        'area': 'mcd',
        'region': [
            {
                "name": "mcd_1",
                "polygon": Polygon([(414, 279), (2, 377), (2, 706), (156, 708), \
                    (495, 538), (720, 338)]),  # Polygon points
                "counts": 0,
                "draggin": False,
                "region_color": (37, 255, 255), # BGR value
                "text_color": (0, 0, 0) # Region text color
            },
            {
                "name": "mcd_2",
                "polygon": Polygon([(727, 340), (880, 708), (1263, 706), (1270, 557), \
                    (959, 343)]),  # Polygon points
                "counts": 0,
                "draggin": False,
                "region_color": (37, 255, 255), # BGR value
                "text_color": (0, 0, 0) # Region text color
            },
        ]
    },
}

FILE_SIZE_THRESHOLD = 800
FRAME_RATE = 12