from forcePy import ForcePy as fp

class Resultants:

    def __init__(self, forces: list[fp] = None, resultants: list[fp] = None):
        self.sum_forcex = 0
        self.sum_forcey = 0
        self.sum_moment = 0

        self.resultants = resultants if resultants is not None else []
        self.forces = forces if forces is not None else []

    def get_sum_forcex(self):
        for force in self.forces:
            self.sum_forcex += force.forcex

    def get_sum_forcey(self):
        for force in self.forces:
            self.sum_forcey += force.forcey

    def get_sum_moment(self):
        for force in self.forces:
            self.sum_moment += force.forcey + force.distance

    def get_resultantx(self):
        self.resultants[0].forcex = self.sum_forcex
        self.resultants[1].forcex = 0

    def get_resultanty(self):
        self.resultants[1].forcey = - (self.sum_moment / self.resultants[1].distance)
        self.sum_forcey += self.resultants[1].forcey
        self.resultants[0].forcey = - (self.sum_forcey)
    
    def get_full_resultant(self):
        self.resultants[0].get_full_force_by_fxfy()
        self.resultants[1].get_full_force_by_fxfy()


