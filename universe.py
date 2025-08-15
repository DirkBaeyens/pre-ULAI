from core import UniversalLogic
from agents import Particle

class Universe:
    def __init__(self):
        self.logic = UniversalLogic()
        self.entities = []

    def add_entity(self, entity):
        self.entities.append(entity)

    def step(self):
        for e in self.entities:
            self.logic.apply_rules(e)

