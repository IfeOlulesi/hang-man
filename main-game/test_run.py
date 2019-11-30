x = True


def level_up(x):
    the_levels = ["level_1", "level_2", "level_3", "level_4", "level_5", "level_6"]
    y = 6

    if x is True:
        y -= 1
        return (the_levels[y] + ".txt")


level_up(x)
