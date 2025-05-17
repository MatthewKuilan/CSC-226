from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from extensions import db

#could add another table for just the radio input choices.
class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str] = mapped_column(unique=True)
    choice: Mapped[str] =  mapped_column()
    house: Mapped[str] = mapped_column(nullable=True)
    wallet_choice: Mapped[str] = mapped_column(nullable=True)
    bully_choice: Mapped[str] = mapped_column(nullable=True)
    challenge_choice: Mapped[str] = mapped_column(nullable=True)
    game_choice: Mapped[str] = mapped_column(nullable=True)
    motivation_choice: Mapped[str] = mapped_column(nullable=True)