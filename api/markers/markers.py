from api.markers import bp

@bp.route('/', methods=['GET'])
def get_markers():
    return {
        "markers": [
            {
                "posX": 0.93,
                "posY": -0.77,
            },
            {
                "posX": -1.4,
                "posY": -0.95,
            },
            {
                "posX": 0.27,
                "posY": 0.41,
            },
            {
                "posX": -2.84,
                "posY": 0.71,
            }
        ]
    }

