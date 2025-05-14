from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from extensions import db

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str] = mapped_column(unique=True)
    choice: Mapped[str] =  mapped_column()
    """house: Mapped[str] = mapped_column(nullable=True)
    house_points: Mapped[str] = mapped_column(nullable=True)"""
