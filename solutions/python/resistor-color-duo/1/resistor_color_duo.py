def value(colors):
    colors = colors[:2]
    color_table = [
            "black",
            "brown",
            "red",
            "orange",
            "yellow",
            "green",
            "blue",
            "violet",
            "grey",
            "white",
        ]

    result = 0

    for color in colors:
        result = result * 10 + color_table.index(color)

    return result
