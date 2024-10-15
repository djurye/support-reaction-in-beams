
from resultants import Resultants

def calculate_resultant(list_force, list_resultant):
    result = Resultants(list_force, list_resultant)
    result.get_sum_forcex()
    result.get_sum_forcey()
    result.get_sum_moment()

    result.get_resultantx()
    result.get_resultanty()

    result.get_full_resultant()

    print("Resultants:")
    print(f"R1 -> Rx = {list_resultant[0].forcex}; Ry = {list_resultant[0].forcey}; module = {list_resultant[0].module}")
    print(f"R2 -> Rx = {list_resultant[1].forcex}; Ry = {list_resultant[1].forcey}; module = {list_resultant[1].module}")