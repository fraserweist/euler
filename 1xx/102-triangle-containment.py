#!/usr/bin/env python

def contains_origin(triangle):
    pos_x = [(x, y) for (x, y) in triangle if x >= 0]
    neg_x = [(x, y) for (x, y) in triangle if x < 0]
    if not pos_x or not neg_x:
        return False
    if len(pos_x) > len(neg_x):
        (x2, y2) = neg_x[0]
        intercepts = []
        for (x1, y1) in (pos_x):
            m = (y2 - y1, x2 - x1)
            y0_numer = y1 * m[1] - m[0] * x1
            y0_denom = 1 * m[1] - m[1] * x1
            if y0_numer == 0:
                return True
            if (y0_numer < 0) + (y0_denom < 0) % 2:
                intercepts.append(-1)
            else:
                intercepts.append(1)
        return 1 in intercepts and -1 in intercepts
    else:
        (x2, y2) = pos_x[0]
        intercepts = []
        for (x1, y1) in (neg_x):
            m = (y2 - y1, x2 - x1)
            y0_numer = y1 * m[1] - m[0] * x1
            y0_denom = 1 * m[1] - m[1] * x1
            if y0_numer == 0:
                return True
            if (y0_numer < 0) + (y0_denom < 0) % 2:
                intercepts.append(-1)
            else:
                intercepts.append(1)
        return 1 in intercepts and -1 in intercepts

if __name__ == "__main__":

    triangles = []
    with open("102-triangle-containment.txt") as file:
        for line in file:
            points = map(lambda x : int(x.strip()), line.split(','))
            triangles.append(((points[0], points[1]), (points[2],points[3]), (points[4],points[5])))

    result = 0
    for triangle in triangles:
        if contains_origin(triangle):
            result += 1
    print result
