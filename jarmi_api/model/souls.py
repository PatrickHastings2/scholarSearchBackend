from sqlalchemy import Column, Integer, String
from .. import db

class Souls(db.Model):
    __tablename__ = "souls"
    id = Column(Integer, primary_key=True)
    _class_name = Column(String, nullable=False)
    _health = Column(Integer, nullable=False)
    _attack = Column(Integer, nullable=False)
    _resistance = Column(Integer, nullable=False)
    _power = Column(Integer, nullable=False)

    def __init__(self, class_name, health, attack, resistance, power):
        self._class_name = class_name
        self._health = health
        self._attack = attack
        self._resistance = resistance
        self._power = power
    
    def __repr__(self):
        return "id='%s', class_name='%s', health='%s', attack='%s', resistance='%s', power='%s'" % (self.id, self.class_name, self.health, self.attack, self.resistance, self.power)
    
    @property
    def class_name(self):
        return self._class_name
    
    @class_name.setter
    def class_name(self, value):
        self._class_name = value

    @property
    def health(self):
        return self._health
    
    @health.setter
    def health(self, value):
        self._health = value
    
    @property
    def attack(self):
        return self._attack
    
    @attack.setter
    def attack(self, value):
        self._attack = value

    @property
    def resistance(self):
        return self._resistance
    
    @resistance.setter
    def resistance(self, value):
        self._resistance = value

    @property
    def power(self):
        return self._power
    
    @power.setter
    def power(self, value):
        self._power = value

    def to_dict(self):
        return {"id": self.id, "class_name": self.class_name, "health": self.health, "attack": self.attack, "resistance": self.resistance, "power": self.power}
    
def init_souls():
    god = Souls(class_name="God", health=10000, attack=10000, resistance=10000, power=1)
    warrior = Souls(class_name="Warrior", health=110, attack=130, resistance=110, power=3)
    knight = Souls(class_name="Knight", health=140, attack=110, resistance=100, power=3)
    wanderer = Souls(class_name="Wanderer", health=100, attack=110, resistance=100, power=3)
    bandit = Souls(class_name="Bandit", health=120, attack=140, resistance=110, power=2)
    hunter = Souls(class_name="Hunter", health=100, attack=140, resistance=110, power=4)
    cleric = Souls(class_name="Cleric", health=130, attack=130, resistance=130, power=3)
    depraved = Souls(class_name="Depraved", health=100, attack=160, resistance=90, power=5)

    db.session.add(god)
    db.session.add(warrior)
    db.session.add(knight)
    db.session.add(wanderer)
    db.session.add(bandit)
    db.session.add(hunter)
    db.session.add(cleric)
    db.session.add(depraved)

    db.session.commit()