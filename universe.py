from core import UniversalLogic

class Universe:
    def __init__(self):
        self.logic = UniversalLogic()
        self.entities = []

    def add_entity(self, entity):
        self.entities.append(entity)

    def step(self):
        # Apply universal logic
        for e in self.entities:
            self.logic.apply_rules(e)
        # Apply interactions between entities
        for i, e1 in enumerate(self.entities):
            for e2 in self.entities[i+1:]:
                e1.apply_interaction(e2)

    def summary(self):
        for e in self.entities:
            print(e)

