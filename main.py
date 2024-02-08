import colorgram
import random
import turtle


def get_colors():
    """return colors from default image"""
    extract_colors = colorgram.extract("hist_spot_painting.jpg", 30)
    color_tuples = []

    for color in extract_colors:
        color_tuple = (color.rgb.r, color.rgb.g, color.rgb.b)
        color_tuples.append(color_tuple)

    return color_tuples

# color_tuples = [(226, 231, 236), (58, 106, 148), (224, 200, 109), (134, 84, 58),
#               (223, 138, 62), (196, 145, 171), (234, 226, 204), (224, 234, 230),
#               (141, 178, 204), (139, 82, 105), (209, 90, 69), (188, 80, 120),
#               (68, 105, 90), (237, 225, 233), (134, 182, 136), (133, 133, 74),
#               (63, 156, 92), (48, 156, 194), (183, 192, 201), (214, 177, 191),
#               (19, 57, 93), (21, 68, 113), (112, 123, 149), (229, 174, 165),
#               (172, 203, 182), (158, 205, 215), (69, 58, 47), (108, 47, 60),
#               (53, 70, 65), (72, 64, 53)]


def draw_hirst_art():
    """main method"""
    turtle.colormode(255)
    spot = turtle.Turtle()
    color_list = get_colors()

    for y in range(-5, 5):
        for x in range(-5, 5):
            spot.teleport(x*60, y*60)
            spot.dot(20, random.choice(color_list))

    canvas = turtle.Screen()
    canvas.exitonclick()


draw_hirst_art()

