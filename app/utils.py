import random
import string
from sqlalchemy.orm import Session
from . import models


def create_db(engine):
    models.Base.metadata.create_all(bind=engine)

    with Session(engine) as session:
        if session.query(models.Roles).first() is not None:
            return

        super_user = models.Roles(description="Super User")
        admin = models.Roles(description="Administrator")
        user = models.Roles(description="User")

        session.add_all([super_user, admin, user])

        session.commit()


def create_random_password():
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(9))

    return password
