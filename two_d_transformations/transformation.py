import math


def translation(v, t):
    for i in range(len(v)):
        for j in range(0, 1):
            x2 = v[i][j] + t[j]
            y2 = v[i][j + 1] + t[j + 1]
            print("Translated coordinates of vertex ", i + 1, " : x2 = ", x2, " ,  y2 = ", y2)
    return


def scaling(v, t):
    for i in range(len(v)):
        for j in range(0, 1):
            x2 = v[i][j] * t[j]
            y2 = v[i][j + 1] * t[j + 1]
            print("Scaled coordinates of vertex ", i + 1, " : x2 = ", x2, " ,  y2 = ", y2)
    return


def rotation(v, o, a, *, cr: bool = False):
    s = math.sin(math.radians(a))
    s = round(s, 2)
    c = math.cos(math.radians(a))
    c = round(c, 2)
    for i in range(len(v)):
        for j in range(0, 1):
            if cr is False:
                x2 = o[j] + ((v[i][j] - o[j]) * c) - ((v[i][j + 1] - o[j + 1]) * s)
                y2 = o[j + 1] + ((v[i][j] - o[j]) * s) + ((v[i][j + 1] - o[j + 1]) * c)
                x2 = round(x2, 2)
                y2 = round(y2, 2)
            else:
                x2 = o[j] + ((v[i][j] - o[j]) * c) + ((v[i][j + 1] - o[j + 1]) * s)
                y2 = o[j + 1] + ((v[i][j] - o[j]) * (-s)) + ((v[i][j + 1] - o[j + 1]) * c)
                x2 = round(x2, 2)
                y2 = round(y2, 2)
            print("Rotated coordinates of vertex ", i + 1, " : x2 = ", x2, " ,  y2 = ", y2)
    return


def shearingx(v, sh):
    for i in range(len(v)):
        for j in range(0, 1):
            x2 = v[i][j] + sh * v[i][j + 1]
            y2 = v[i][j + 1]
            print("Along x-axis, sheared coordinates of vertex ", i + 1, " : x2 = ", x2, " ,  y2 = ", y2)
    return


def shearingy(v, sh):
    for i in range(len(v)):
        for j in range(0, 1):
            x2 = v[i][j]
            y2 = v[i][j + 1] + sh * v[i][j]
            print("Along y-axis, sheared coordinates of vertex ", i + 1, " : x2 = ", x2, " ,  y2 = ", y2)
    return


def reflectionx(v):
    for i in range(len(v)):
        for j in range(0, 1):
            x2 = v[i][j]
            y2 = -v[i][j + 1]
            print("Along x-axis, reflected coordinates of vertex ", i + 1, " : x2 = ", x2, " ,  y2 = ", y2)
    return


def reflectiony(v):
    for i in range(len(v)):
        for j in range(0, 1):
            x2 = -v[i][j]
            y2 = v[i][j + 1]
            print("Along y-axis, reflected coordinates of vertex ", i + 1, " : x2 = ", x2, " ,  y2 = ", y2)
    return


def reflectionorigin(v):
    for i in range(len(v)):
        for j in range(0, 1):
            x2 = -v[i][j]
            y2 = -v[i][j + 1]
            print("About origin, reflected coordinates of vertex ", i + 1, " : x2 = ", x2, " ,  y2 = ", y2)
    return


def reflectionxy(v):
    for i in range(len(v)):
        for j in range(0, 1):
            x2 = v[i][j + 1]
            y2 = v[i][j]
            print("About X+Y, reflected coordinates of vertex ", i + 1, " : x2 = ", x2, " ,  y2 = ", y2)
    return
