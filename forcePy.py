import json
from param_given import Param_given as pg, param_mappings
from math import sqrt, atan,cos, sin, radians, pi


class ForcePy():

    def __init__(self, distance, param_given: pg = None, param1_value = None, param2_value = None):
        self.distance = float
        self.relative_distance = float
        self.module = float
        self.forcex = float
        self.forcey = float
        self.nvector = str
        self.teta = float | str
        self.tetadegree = float
        self.distance = distance

        if param_given is not None:
            self.param_given = param_given
            param1_name, param2_name = param_mappings[param_given]
            setattr(self, param1_name, param1_value)
            setattr(self, param2_name, param2_value)

        if (param1_value is not None) and (param2_value is not None): 
            self.get_full_force()


    def get_full_force(self):
        match self.param_given:
            case pg.DECOMPOSED_FORCES:
                self.get_full_force_by_fxfy()
            case pg.MODULE_TETA:
                self.transform_teta_in_rad()
                self.get_full_force_by_teta_module()
            case pg.MODULE_NVECTOR:
                self.get_full_force_by_nvector_module()
                

    def get_full_force_by_fxfy(self):
        self.find_module_by_fxfy()
        self.find_nvector_by_fxfy()
        self.find_teta_by_fxfy()

    def get_full_force_by_nvector_module(self):
        self.find_fxfy_by_nvector()
        self.find_teta_by_fxfy()

    def get_full_force_by_teta_module(self):
        self.find_fxfy_by_teta()
        self.find_nvector_by_fxfy()

    def transform_teta_in_rad(self):
        if str(self.teta).find("°") != -1:
            self.teta = round(radians(float(self.teta.replace("°",""))),5)
        else:
            self.teta = round(radians(float(self.teta)),5)

    def find_module_by_fxfy(self):
        self.module = round(sqrt(self.forcex**2 + self.forcey**2),5)
        return

    def find_nvector_by_fxfy(self):
        if self.module==0: 
            self.find_module_by_fxfy()
        
        if self.module==0:
            nx, ny = 0, 0
        else:
            nx = round(self.forcex / self.module,4)
            ny = round(self.forcey / self.module,4)

        self.nvector = f"{nx}i {ny}j"

    def find_teta_by_fxfy(self):
        aux_angle = 0
        if self.forcex < 0:
            aux_angle = pi
        elif self.forcey < 0 and self.forcex >= 0:
            aux_angle = 2 * pi

        if self.forcex == 0:
            if self.forcey > 0:
                self.teta = pi/2
            elif self.forcey < 0:
                self.teta = 3*pi/2
            else:
                self.teta = 0
        elif self.forcey != 0:
            self.teta = aux_angle + round(atan(self.forcey/self.forcex),5)
        else:
            self.teta = 0

        self.tetadegree = self.teta * (180 / pi)

    def find_fxfy_by_nvector(self):
        nlist = self.nvector.replace("i","").replace("j","").split()
        self.forcex = round(self.module * float(nlist[0]),5)
        self.forcey = round(self.module * float(nlist[1]),5)

    def find_fxfy_by_teta(self):
        self.tetadegree = self.teta * (180 / pi)
        self.forcex = round(self.module * cos(self.teta),3)
        self.forcey = round(self.module * sin(self.teta),3)
