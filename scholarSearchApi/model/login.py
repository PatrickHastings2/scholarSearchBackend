from sqlalchemy import Column, Integer, String
from .. import db

class Login(db.Model):
    __tablename__ = "login"
    id = Column(Integer, primary_key=True)
    _username = Column(String, nullable=False)
    _password = Column(String, nullable=False)

    def __init__(self, username, password):
        self._username = username
        self._password = password
    
    def __repr__(self):
        return "id='%s', username='%s', password='%s'" % (self.id, self.username, self.password)
    
    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, value):
        self._username = value

    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, value):
        self._password = value

    def to_dict(self):
        return {"id": self.id, "username": self.username, "password": self.password}
    
def init_login():
    admin = Login(username="admin", password="admin")
    user1 = Login(username="user1", password="123456")
    user2 = Login(username="user2", password="password")
    
    db.session.add(admin)
    db.session.add(user1)
    db.session.add(user2)

    db.session.commit()
