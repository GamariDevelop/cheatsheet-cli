import re
import json
import os
import uuid
import fire

from src.utils import cprint, log, CheatList

# ファイル保存の場所はapp.pyと同じディレクトリ
dir_path = os.path.join(os.path.dirname(__file__), "output")
file_path = os.path.join(dir_path, "urls.json")


class Command(object):
    def list(self):
        """コマンド一覧を表示"""
        print("PAHT", file_path)
        try:
            with open(file_path) as cheats_file:
                cheats = json.load(cheats_file)
                cheat_list = CheatList(cheats)
        except FileNotFoundError:
            return "addコマンドで、コマンドを追加してください。"

        cheat_list.print_list()

    def add(self, app: str, cmd: str, description: str) -> str:
        """URLの追加を行う。"""

        # ファイルが存在しない場合は新規作成
        if not os.path.exists(file_path):
            os.makedirs(dir_path, exist_ok=True)
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
                cheat_list = CheatList(cheats_dict)
        except FileNotFoundError:
            return "削除するコマンドがありません。"

        if not cheat_list.has_commands(app):
            return "削除するコマンドがありません。"
        questions = cheat_list.create_questions(app)

        answer = inquirer.prompt([
            inquirer.List(
                "command",
                message="削除するコマンドを選択してください。",
                choices=questions
            ),
        ])

        target_id = None
        for c in cheat_list.get_commands(app):
            print(c, answer)
            if str(c) == answer["command"]:
                target_id = c["id"]

        # delete処理
        cheat_list.delete(app, target_id)

        with open(file_path, "w") as write_file:
            json.dump(cheat_list.get(), write_file, indent=4)


def main():
    fire.Fire(Command)


if __name__ == "__main__":
    main()
