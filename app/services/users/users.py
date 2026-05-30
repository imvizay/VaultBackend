from sqlalchemy.orm import Session
from app.models.user_model import User


def fetch_all_users(db: Session):

    users = db.query(User).all()

    return users