from vector import Vector


try:
    v1 = Vector(-3)
except ValueError as e:
    print("ValueError :", e)
else:
    print(v1)
    v2 = v1 + 1
    print(v2)
    v3 = 1 * v2
    print(v3)
