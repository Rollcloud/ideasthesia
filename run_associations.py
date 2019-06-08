from colored import fg, bg, attr
from colours import colours

def colour_input(text):
    reset = attr('reset')
    for char in text:
        try:
            colour = fg('black') + bg(colours[char])
        except KeyError:
            colour = reset
        print(colour + char + reset, end="")
    print()

if __name__ == "__main__":
    print("Please enter a word or number:")
    try:
        while True:
            colour_input(input())
    except KeyboardInterrupt:
        pass
