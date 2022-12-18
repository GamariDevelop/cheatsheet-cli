import re
import json
import os
import uuid
import fire

from utils import cprint, log, CheatList

# ファイル保存の場所はapp.pyと同じディレクトリ
file_path = os.path.dirname(__file__) + "\\urls.json"


class Command(object):
    def list(self):
        """コマンド一覧を表示"""
        try:
            with open(file_path) as cheats_file:
                cheats = json.load(cheats_file)
        except FileNotFoundError:
            return "addコマンドで、URLを追加してください。"

        for cheat_name, cheat in cheats.items():
            print(cheat_name)
            for cmd in cheat["commands"]:
                print(f"  {cmd['command']} | {cmd['description']}")

    def add(self, app: str, cmd: str, description: str) -> str:
        """URLの追加を行う。"""
        file_path = os.path.join(os.path.dirname(__file__), "urls.json")

        # ファイルが存在しない場合は新規作成
        if not os.path.exists(file_path):
            with open(file_path, "w") as f:
                f.write("{}")

        # 読み込み
        with open(file_path, "r") as cheats_file:
            cheats = json.load(cheats_file)
            cheat_list = CheatList(cheats)

        cheat_list.add_command(app, cmd, description)

        # 追加処理
        with open(file_path, "w") as write_file:
            json.dump(cheat_list.get(), write_file, indent=4)

        return "追加完了"

    def delete(self, app: str):
        """コマンド削除"""
        import re
        import inquirer
        questions = []
        try:
            with open(file_path) as cheats_file:
                cheats_dict = json.load(cheats_file)
                target_cheat_commands = cheats_dict[app]["commands"]
                for command in target_cheat_commands:
                    questions.append(str(command))
        except FileNotFoundError:
            return "削除するコマンドがありません。"

        # コマンドのバグがある
        log(questions)
        answers = inquirer.prompt([
            inquirer.List(
                "command",
                message="削除するコマンドを選択してください。",
                choices=questions
            ),
        ])
        log(answers)


def main():
    fire.Fire(Command)


if __name__ == "__main__":
    main()
