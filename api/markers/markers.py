from flask import Response, request
from api.extensions import db
from api.markers import bp
from api.models.marker import Marker


@bp.route('/', methods=['GET'])
def get_markers():
    return {
        "markers": Marker.query.all()
    }


@bp.route('/', methods=['POST'])
def add_marker():
    pos_x = request.args.get('posX')
    pos_y = request.args.get('posY')

    if pos_x and pos_y:
        existing_marker = Marker.query.filter(
            Marker.posX == pos_x or Marker.posY == pos_y
        )

        if existing_marker:
            return Response("Markers already exist", status=409)

        new_marker = Marker(
            pos_x=pos_x,
            pos_y=pos_y
        )
        db.session.add(new_marker)
        db.session.commit()

    return Response(status=201)
