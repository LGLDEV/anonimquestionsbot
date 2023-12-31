from .database import session
from models import User, Admin


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

    def get_users(self):
        users = self.query.all()
        return users

    def get_count(self):
        return self.query.count()

    # admin querys
    def get_admin(self, admin_id):
        admins = self.query.filter(self.model.admin_id == admin_id)
        for admin in admins:
            return admin

            
    def create_admin(self, admin_id, admin_role):
        session.add(Admin(admin_id=admin_id, admin_role=admin_role))
        session.commit()

    def delete_admin(self, admin_id):
        admin = self.query.filter_by(admin_id=admin_id).one_or_none()
        session.delete(admin)
        session.commit()
