import uuid
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


def log(str: str):
    pprint.pprint(str)


class CheatList(object):
    def __init__(self, data):
        self.before = data
        self.cheat_list = data

    def get(self):
        return self.cheat_list

    def has_cheat(self, app: str):
        if self.cheat_list.get(app) is not None:
            return True
        else:
            return False

    def add_command(self, app: str, command: str, description: str):
        """コマンドの追加処理。"""
        if not self.has_cheat(app):
            self.cheat_list[app] = {
                "commands": []
            }

        update_commands = self.cheat_list[app].get("commands")
        update_commands.append({
            "id": str(uuid.uuid4()),
            "command": command,
            "description": description
        })
        log(update_commands)

    ### 表示系 ###
    def print(self):
        log(self.cheat_list)

    def print_list(self):
        for cheat_name, cheat in self.cheat_list.items():
            cprint(cheat_name, "BLUE")
            for cmd in cheat["commands"]:
                print(f"  {cmd['command']} | {cmd['description']}")
