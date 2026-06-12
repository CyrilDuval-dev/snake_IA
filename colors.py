class Colors:
    green = (132, 189, 53)
    light_green = (167, 217, 71)
    red = (231, 87, 90)
    blue = (73, 119, 237)
    dark_green = (86, 138, 52)
    white = (255, 255, 255)

    @classmethod
    def get_cell_colors(cls):
        return [cls.green, cls.light_green, cls.red, cls.blue, cls.dark_green]