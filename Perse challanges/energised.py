def KE(m,v) -> float:
    return 0.5 * m * (v**2)

def GPE(m,h) -> float:
    return m * 10 * h

mass = int(input())
speed = int(input())
height = int(input())

me = KE(mass,speed) + GPE(mass,height)
print(round(me,1))
