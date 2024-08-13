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
                "polygon": Polygon([(535, 316), (0, 471), (4, 713), (135, 713), \
                    (519, 521), (720, 342)]),  # Polygon points
                "counts": 0,
                "draggin": False,
                "region_color": (37, 255, 255), # BGR value
                "text_color": (0, 0, 0) # Region text color
            },
            {
                "name": "mcd_2",
                "polygon": Polygon([(731, 338), (808, 536), (880, 705), (1265, 703), \
                    (1270, 637), (994, 381)]),  # Polygon points
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