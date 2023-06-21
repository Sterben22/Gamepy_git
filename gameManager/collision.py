import math
class Collision():
    def __init__(self) -> None:
        pass

    def isCollision(x1, x2, y1, y2):
        distance = math.sqrt((math.pow(x1 - x2,2)) + (math.pow(y1 - y2,2)))
        if distance <= 50:
            return True
        else:
            return False