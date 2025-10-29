from api.extensions import db

class Marker(db.Model):
    """Data model for map markers"""
    id = db.Column(
        db.Integer,
        primary_key=True
    )

    pos_x = db.Column(
        db.Float,
        index=False,
        unique=False,
        nullable=False
    )

    pos_y = db.Column(
        db.Float,
        index=False,
        unique=False,
        nullable=False
    )

    def to_dict(self):
        """Serializes marker data to a dictionary"""
        return {
            'id': self.id,
            'posX': self.pos_x,
            'posY': self.pos_y
        }

    def __repr__(self):
        return '<Marker {}>'.format(self.id)