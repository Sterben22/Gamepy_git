import math

def isCollision(player, enemy):
    distance = math.sqrt((math.pow(player.x - enemy.x,2)) + (math.pow(player.y - enemy.y,2)))
    if distance <= 15:
        return True
    else:
        return False