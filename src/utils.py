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

    def get_commands(self, app: str):
        return self.cheat_list[app].get("commands")

    def create_questions(self, app: str):
        if not self.has_cheat(app):
            return []
        else:
            commands = self.get_commands(app)
            questions = []
            for cmd in commands:
                questions.append(str(cmd))
            return questions

    ### 判定系 ###
    def has_cheat(self, app: str):
        if self.cheat_list.get(app) is not None:
            return True
        else:
            return False

    def has_commands(self, app: str):
        if len(self.cheat_list.get(app)["commands"]) == 0:
            return False
        else:
            return True

    ### 更新系 ###
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

    def delete(self, app: str, target_id: str):
        update_commands = [
            item for item in self.cheat_list[app].get("commands") if item["id"] != target_id]
        self.cheat_list[app]["commands"] = update_commands

    ### 表示系 ###
    def print(self):
        log(self.cheat_list)

    def print_list(self):
        for cheat_name, cheat in self.cheat_list.items():
            # cprint(cheat_name, "BLUE")    # TODO 色を付けるように変更する
            print(cheat_name, "BLUE")
            for cmd in cheat["commands"]:
                print(f"  {cmd['command']} | {cmd['description']}")
