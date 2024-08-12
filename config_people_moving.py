from shapely.geometry import Polygon

LOCATION_CONF = {
    'tsu': {
        'host': '182.0.22.141:554/ch2/main',
        'username': 'admin',
        'password': 'CZADKZ',
        'area': 'tsu',
        'region': [
            {
                "name": "tsu_1",
                "polygon": Polygon([(0, 0), (0, 720), (1270, 720), (1270, 0)]),  # Polygon points
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
        'region': [
            {
                "name": "mcd_1",
                "polygon": Polygon([(0, 0), (0, 720), (1270, 720), (1270, 0)]),  # Polygon points
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
        'region': [
            {
                "name": "masjid_1",
                "polygon": Polygon([(0, 0), (0, 720), (1270, 720), (1270, 0)]),  # Polygon points
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
        'region': [
            {
                "name": "sol_1",
                "polygon": Polygon([(0, 0), (0, 720), (1270, 720), (1270, 0)]),  # Polygon points
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
        'region': [
            {
                "name": "spklu_1",
                "polygon": Polygon([(0, 0), (0, 720), (1270, 720), (1270, 0)]),  # Polygon points
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
        'region': [
            {
                "name": "cig_1",
                "polygon": Polygon([(0, 0), (0, 720), (1270, 720), (1270, 0)]),  # Polygon points
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
        'region': [
            {
                "name": "stb_1",
                "polygon": Polygon([(0, 0), (0, 720), (1270, 720), (1270, 0)]),  # Polygon points
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
        'region': [
            {
                "name": "toilet_1",
                "polygon": Polygon([(0, 0), (0, 720), (1270, 720), (1270, 0)]),  # Polygon points
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