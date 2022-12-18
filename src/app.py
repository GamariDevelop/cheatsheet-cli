import re
import json
import webbrowser
import os

import fire

from utils import cprint

# ファイル保存の場所はapp.pyと同じディレクトリ
file_path = os.path.dirname(__file__) + "\\urls.json"


class Command(object):
    def list(self):
        """コマンド一覧を表示"""
        try:
            with open(file_path) as cheats_file:
                cheats_dict = json.load(cheats_file)
                print(cheats_dict)
                for cheat_name in cheats_dict:
                    cprint(cheat_name, color="blue")
                    for cmd_dict in cheats_dict[cheat_name]["commands"]:
                        command = cmd_dict["command"]
                        description = cmd_dict["description"]
                        print("  ", command, " | ", description)
        except FileNotFoundError:
            return "addコマンドで、URLを追加してください。"

    def add(self, app: str, command: str) -> str:
        """URLの追加を行う。"""
        file_path = os.path.dirname(__file__) + "\\urls.json"

        # ファイルが存在しない場合は新規作成
        if not os.path.exists(file_path):
            with open(file_path, 'w') as f:
                f.write("{}")

        # 読み込み
        with open(file_path, "r") as cheats_file:
            cheats_dict = json.load(cheats_file)

            # サイト名が重複している場合はエラー
            for cheats in cheats_dict:
                if url_map["app"] == app:
                    return "サイト名が重複しています。別の名前で登録してください。"

            # URL形式の判定
            url_pattern = "https?://[\w/:%#\$&\?\(\)~\.=\+\-]+"
            if not re.match(url_pattern, url):
                return "URLの形式が間違っています。確認してください。"

            # 追加処理
            with open(file_path, "w") as write_file:
                urls_dict.append({"app": app, "url": url})
                json.dump(urls_dict, write_file, indent=4)

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
        print(questions)
        answers = inquirer.prompt([
            inquirer.List(
                "command",
                message="削除するコマンドを選択してください。",
                choices=questions
            ),
        ])
        print(answers)


def main():
    fire.Fire(Command)


if __name__ == "__main__":
    main()
