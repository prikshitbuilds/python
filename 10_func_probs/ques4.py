import math

def circle_stats(radius):
    area=math.pi * (radius **2)
    circum= 2 * math.pi * radius
    return area,circum

area,circum =circle_stats(3)
print(f"area of circle is {area:.2f}")
