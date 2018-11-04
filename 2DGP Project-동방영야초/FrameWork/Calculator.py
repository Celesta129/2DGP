import math


def collision_circle_circle(ob1, ob2):
    dist = cal_dist(ob1.ObjectInfo, ob2.ObjectInfo)

    radius = ob1.ObjectInfo.width
    if dist < radius:
        return True
    else:
        return False

def collision_rect_rect(ob1, ob2):
    pts1 = (ob1.ObjectInfo.x, ob1.ObjectInfo.y)
    pts2 = (ob2.ObjectInfo.x, ob2.ObjectInfo.y)
    ob1_points = [[pts1[0] - ob1.ObjectInfo.width*0.5 ,pts1[1] - ob1.ObjectInfo.height*0.5],
                 [pts1[0] - ob1.ObjectInfo.width*0.5 ,pts1[1] + ob1.ObjectInfo.height*0.5],
                 [pts1[0] + ob1.ObjectInfo.width*0.5 ,pts1[1] + ob1.ObjectInfo.height*0.5],
                 [pts1[0] + ob1.ObjectInfo.width*0.5, pts1[1] - ob1.ObjectInfo.height*0.5]]

    ob2_points = [[pts2[0] - ob2.ObjectInfo.width*0.5 ,pts2[1] - ob2.ObjectInfo.height*0.5],
                 [pts2[0] - ob2.ObjectInfo.width*0.5 ,pts2[1] + ob2.ObjectInfo.height*0.5],
                 [pts2[0] + ob2.ObjectInfo.width*0.5 ,pts2[1] + ob2.ObjectInfo.height*0.5],
                 [pts2[0] + ob2.ObjectInfo.width*0.5, pts2[1] - ob2.ObjectInfo.height*0.5]]

    ob1_lines = [[ob1_points[0],ob1_points[1]], [ob1_points[1],ob1_points[2]],
                 [ob1_points[2],ob1_points[3]], [ob1_points[3],ob1_points[0]]]

    ob2_lines = [[ob2_points[0],ob2_points[1]], [ob2_points[1],ob2_points[2]],
                 [ob2_points[2],ob2_points[3]], [ob2_points[3],ob2_points[0]]]
    ## rotate 감안
    # if ob1.ObjectInfo.rot != 0.0:
    #     for ob1_line in ob1_lines:
    #         for i in range(2):
    #             radian = math.radians(ob1.ObjectInfo.rot)
    #             x = (ob1_line[i][0] - pts1[0]) * math.cos(radian) + (ob1_line[i][1] - pts1[1]) * -math.sin(radian)
    #             y = (ob1_line[i][0] - pts1[0]) * math.sin(radian) + (ob1_line[i][1] - pts1[1]) * math.cos(radian)
    #             ob1_line[i][0] = pts1[0] + x
    #             ob1_line[i][1] = pts1[1] + y
    #
    # if ob2.ObjectInfo.rot != 0.0:
    #     for ob2_line in ob2_lines:
    #         for i in range(2):
    #             radian = math.radians(ob2.ObjectInfo.rot)
    #             x = (ob2_line[i][0] - pts2[0]) * math.cos(radian) + (ob2_line[i][1] - pts2[1]) * -math.sin(radian)
    #             y = (ob2_line[i][0] - pts2[0]) * math.sin(radian) + (ob2_line[i][1] - pts2[1]) * math.cos(radian)
    #             ob2_line[i][0] = pts2[0] + x
    #             ob2_line[i][1] = pts2[1] + y
    #
    # for ob1_line in ob1_lines:
    #     for ob2_line in ob2_lines:
    #         if collision_line_line(ob1_line,ob2_line) == True:
    #             return True

    for point in ob1_points:
            if ob2_points[0][1] <= point[1] and point[1] <= ob2_points[1][1]:
                if ob2_points[1][0] <= point[0] and point[0] <= ob2_points[2][0]:
                    return True
    for point in ob2_points:
            if ob1_points[0][1] <= point[1] and point[1] <= ob1_points[1][1]:
                if ob1_points[1][0] <= point[0] and point[0] <= ob1_points[2][0]:
                    return True
    return False
    pass


def collision_line_line(line1, line2):
    x1, y1 = line1[0]
    x2, y2 = line1[1]

    x3, y3 = line2[0]
    x4, y4 = line2[1]

    u = ((x4 - x3) * (y1 - y3) - (y4 - y3) * (x1 - x3)) / ((x2 - x1) * (y4 - y3) - (x4 - x3) * (y2 - y1))
    v = ((x2 - x1) * (y1 - y3) - (y2 - y1) * (x1 - x3)) / ((x2 - x1) * (y4 - y3) - (x4 - x3) * (y2 - y1))

    if ((0 < u and u < 1) and
        (0 < v and v < 1)):
        return True

    return False


def cal_dist(pt1, pt2):
    dist = math.sqrt((pt2.x - pt1.x)**2 + (pt2.y - pt1.y)**2)
    return dist

def collision_rect_circle(ob1,ob2):

    pass

def collision(ob1, ob2):
    ob1Type = ob1.ObjectInfo.objectType
    ob2Type = ob2.ObjectInfo.objectType

    if ob1Type == "Rect" and ob2Type == "Rect":
        return collision_rect_rect(ob1,ob2)
    elif ob1Type == "Rect" and ob2Type == "Circle":
        return collision_rect_circle(ob1,ob2)
    elif ob1Type == "Circle" and ob2Type == "Rect":
        return collision_rect_circle(ob2,ob1)
    else: # ob1Type == "Circle" and ob2Type == "Circle":   or etc...
        return collision_circle_circle(ob1,ob2)
    pass

