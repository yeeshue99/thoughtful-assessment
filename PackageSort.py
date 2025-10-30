SIZE_MAX = 1000000
LENGTH_MAX = 150
WEIGHT_MAX = 20

def sort(width: float, height: float, length: float, mass: float) -> str:
    bulky = False
    heavy = False

    if any(dimension < 0 for dimension in [width, height, length, mass]):
        raise ValueError("All dimensions must be non-negative")

    if any(dimension >= LENGTH_MAX for dimension in [width, height, length]):
        bulky = True
    elif width * height * length >= SIZE_MAX:
        bulky = True

    if mass >= WEIGHT_MAX:
        heavy = True

    if bulky and heavy:
        return "Reject"

    if bulky or heavy:
        return "Special"

    return "Accept"
