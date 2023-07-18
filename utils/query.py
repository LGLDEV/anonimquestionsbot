from .database import session
from models import User


class Query:
    def __init__(self, model) -> None:
        self.model = model
        self.query = session.query(self.model)

    def get_user(self, user_id):
        user = self.query.filter(self.model.user_id == user_id)
        for u in user:
            return u
    
    def create_user(self, user_id):
        session.add(User(user_id=user_id, lang='lang'))
        session.commit()


