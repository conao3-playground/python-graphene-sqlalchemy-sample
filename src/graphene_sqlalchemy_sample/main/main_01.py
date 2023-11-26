from __future__ import annotations

import sqlalchemy as sa
import sqlalchemy.orm as sa_orm


engine = sa.create_engine("sqlite:///:memory:", echo=True)
session = sa_orm.Session(engine)


@sa_orm.as_declarative()
class Base:
    def __repr__(self) -> str:
        args = ", ".join(
            [
                f"{key}={repr(val)}"
                for key, val in self.__dict__.items()
                if not key.startswith("_")
            ],
        )
        return f"{self.__class__.__name__}({args})"


class User(Base):
    __tablename__ = "user"

    user_id = sa.Column(sa.String(32), primary_key=True)
    name = sa.Column(sa.String(32), nullable=False)
    age = sa.Column(sa.Integer, nullable=False)


def init_db() -> None:
    Base.metadata.create_all(engine)
    session.add_all(
        [
            User(user_id="user_01", name="user_01", age=10),
            User(user_id="user_02", name="user_02", age=20),
            User(user_id="user_03", name="user_03", age=30),
        ],
    )
    session.commit()


def main() -> None:
    init_db()
    print(session.query(User).all())
