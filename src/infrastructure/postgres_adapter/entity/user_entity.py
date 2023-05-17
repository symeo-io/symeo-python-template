from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class UserEntity(Base):
    __tablename__ = "users"

    id: Mapped[str] = mapped_column(String(30), primary_key=True)
    username: Mapped[str] = mapped_column(String(30))
