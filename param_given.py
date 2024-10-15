from enum import Enum

class Param_given(Enum):
    DECOMPOSED_FORCES = 1
    MODULE_TETA = 2
    MODULE_NVECTOR = 3

param_mappings = {
    Param_given.DECOMPOSED_FORCES: ("forcex", "forcey"),
    Param_given.MODULE_TETA: ("module", "teta"),
    Param_given.MODULE_NVECTOR: ("module", "nvector")
}