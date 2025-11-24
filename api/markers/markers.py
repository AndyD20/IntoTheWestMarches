from flask import Response, request, make_response
from api.extensions import db
from api.markers import bp
from api.models.marker import Marker


@bp.route('/', methods=['GET'])
def get_markers():
    markers = Marker.query.all()

    return make_response({
        "markers": [marker.to_dict() for marker in markers]
    }, 200)


@bp.route('/', methods=['POST'])
def add_marker():
    pos_x = request.args.get('pos_x')
    pos_y = request.args.get('pos_y')
    type = request.args.get('type')

    if not (pos_x and pos_y and type):
        return Response("Missing pos_x or pos_y or type parameters", status=400)

    existing_marker = Marker.query.filter(
        Marker.pos_x == pos_x and Marker.pos_y == pos_y and Marker.type == type
    ).first()

    if existing_marker:
        return Response("Marker already exists", status=409)    

    new_marker = Marker(
        pos_x=pos_x,
        pos_y=pos_y,
        type=type
    )
    db.session.add(new_marker)
    db.session.commit()

    return make_response(status=201)
