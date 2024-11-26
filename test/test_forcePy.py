import enums.param_given as pg

from models.forcePy import ForcePy
from models.resultants import Resultants
import index

f0 = ForcePy(2, pg.Param_given.DECOMPOSED_FORCES, 3, 4)

f1 = ForcePy(3, pg.Param_given(1), 20, 4)

f2 = ForcePy(18, pg.Param_given.MODULE_TETA, 5, "180°")

f3 = ForcePy(4, pg.Param_given.MODULE_NVECTOR, 8, "0.97014i 0.24254j")

r1 = ForcePy(0)
r2 = ForcePy(20)

index.calculate_resultant([f0, f1, f2, f3], [r1,r2])



print(":)")