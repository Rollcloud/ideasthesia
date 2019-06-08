from colored import fg, bg, attr, colored

c = colored("black")

reset = attr('reset')
for col, value in c.paint.items():
    colour = fg('black') + bg(col)
    print(colour + col + reset)
