from shapely.geometry import Polygon

LOCATION_CONF = {
    'tsu': {
        'host': '182.0.22.141:554/ch2/main',
        'username': 'admin',
        'password': 'CZADKZ',
        'area': 'tsu',
        'max_capacity': [10],
        'region': [
            {
                "name": "tsu_1",
                "polygon": Polygon([(353, 662), (1180, 355), (711, 148), (174, 245)]),  # Polygon points
                "counts": 0,
                "draggin": False,
                "region_color": (37, 255, 255), # BGR value
                "text_color": (0, 0, 0) # Region text color
            },
        ]
    },
    'mcd': {
        'host': '182.0.21.152:554/ch1/main',
        'username': 'admin',
        'password': 'IMGTDW',
        'area': 'mcd',
        'max_capacity': [10],
        'region': [
            {
                "name": "mcd_1",
                "polygon": Polygon([(293, 325), (521, 409), (746, 315), (568, 265)]),  # Polygon points
                "counts": 0,
                "draggin": False,
                "region_color": (37, 255, 255), # BGR value
                "text_color": (0, 0, 0) # Region text color
            },
        ]
    },
    'masjid': {
        'host': '182.0.23.101:554/ch2/main',
        'username': 'admin',
        'password': 'XNJELA',
        'area': 'masjid',
        'max_capacity': [10],
        'region': [
            {
                "name": "masjid_1",
                "polygon": Polygon([(362, 61), (165, 115), (0, 687), (1265, 316), \
                    (797, 106)]),  # Polygon points
                "counts": 0,
                "draggin": False,
                "region_color": (37, 255, 255), # BGR value
                "text_color": (0, 0, 0) # Region text color
            },
        ]
    },
    'sol': {
        'host': '182.0.20.72:554/ch1/main',
        'username': 'admin',
        'password': 'WCMWNA',
        'area': 'sol',
        'max_capacity': [10],
        'region': [
            {
                "name": "sol_1",
                "polygon": Polygon([(77, 534), (437, 702), (722, 702), (784, 492), (459, 363)]),  # Polygon points
                "counts": 0,
                "draggin": False,
                "region_color": (37, 255, 255), # BGR value
                "text_color": (0, 0, 0) # Region text color
            },
        ]
    },
    'spklu': {
        'host': '182.0.20.72:554/ch2/main',
        'username': 'admin',
        'password': 'WCMWNA',
        'area': 'spklu',
        'max_capacity': [10],
        'region': [
            {
                "name": "spklu_1",
                "polygon": Polygon([(125, 366), (527, 680), (1201, 444), (843, 278)]),  # Polygon points
                "counts": 0,
                "draggin": False,
                "region_color": (37, 255, 255), # BGR value
                "text_color": (0, 0, 0) # Region text color
            },
        ]
    },
    'cig': {
        'host': '182.0.23.170:554/ch1/main',
        'username': 'admin',
        'password': 'FNZLLZ',
        'area': 'cig',
        'max_capacity': [10],
        'region': [
            {
                "name": "cig_1",
                "polygon": Polygon([(149, 312), (838, 464), (887, 340), (269, 238)]),  # Polygon points
                "counts": 0,
                "draggin": False,
                "region_color": (37, 255, 255), # BGR value
                "text_color": (0, 0, 0) # Region text color
            },
        ]
    },
    'stb': {
        'host': '182.0.21.189:554/ch2/main',
        'username': 'admin',
        'password': 'WGNVQB',
        'area': 'stb',
        'max_capacity': [10],
        'region': [
            {
                "name": "stb_1",
                "polygon": Polygon([(111, 261), (61, 383), (205, 429), (173, 670), \
                    (1179, 535), (647, 279)]),  # Polygon points
                "counts": 0,
                "draggin": False,
                "region_color": (37, 255, 255), # BGR value
                "text_color": (0, 0, 0) # Region text color
            },
        ]
    },
    'toilet': {
        'host': '182.0.21.152:554/ch2/main',
        'username': 'admin',
        'password': 'IMGTDW',
        'area': 'toilet',
        'max_capacity': [10],
        'region': [
            {
                "name": "toilet_1",
                "polygon": Polygon([(359, 188), (185, 323), (372, 333), (349, 465), \
                    (1069, 409), (855, 200)]),  # Polygon points
                "counts": 0,
                "draggin": False,
                "region_color": (37, 255, 255), # BGR value
                "text_color": (0, 0, 0) # Region text color
            },
        ]
    },
}

FILE_SIZE_THRESHOLD = 500
FRAME_RATE = 12