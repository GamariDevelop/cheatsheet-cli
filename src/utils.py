import pprint


class Color(object):
    RED = '\033[31m'
    BLUE = '\033[34m'
    YELLOW = '\033[33m'
    RESET = '\033[0m'


def cprint(str, color=None):
    """色をつけて表示する。"""
    if color == "red" or color == "RED":
        print(f'{Color.RED}{str}{Color.RESET}')
    elif color == "blue" or color == "BLUE":
        print(f'{Color.BLUE}{str}{Color.RESET}')
    else:
        print(str)

# def


def log(str: str):
    pprint.pprint(str)
