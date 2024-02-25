from datetime import datetime
from apps.main import db


class Dreampost(db.MOdel):

    __tablename__ = 'posted'

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )
    # title
    title = db.Column(
        db.String(200),
        nullable=False
    )
    # main contents
    contents = db.Column(
        db.Text,
        nullable=False
    )
    # post date
    create_at = db.Column(
        db.Date,
        default=datetime.today()
    )
