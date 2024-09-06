
import math
from decimal import Decimal, ROUND_HALF_UP

def angleCalculater(pt1, pt2):

    [x1,y1] = pt1
    [x2,y2] = pt2

    dx = x2 - x1
    dy = y2 - y1

    angle_radians = math.atan2(dy, dx)
    angle_degrees = math.degrees(angle_radians)
    angle_degrees = round(angle_degrees,2)
    

    if angle_degrees < 0:
        angle_degrees += 360

    angle_degrees = 360 - angle_degrees
    value = Decimal(angle_degrees)

    rounded_value = value.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

    round_value = float(rounded_value)

    return round_value

if __name__ == "__main__":
    pt2 = [1, 1.1]
    pt1 = [0, 0]
    angle = angleCalculater(pt1, pt2)
    print(f"angle is: {angle}°")
