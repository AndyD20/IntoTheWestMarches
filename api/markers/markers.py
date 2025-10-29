from api.markers import bp

@bp.route('/', methods=['GET'])
def get_markers():
    return {
        "markers": [
            {
                "posX": 100,
                "posY": 100,
            },
            {
                "posX": 200,
                "posY": 200,
            },
            {
                "posX": 300,
                "posY": 300,
            }
        ]
    }

