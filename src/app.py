import re
import json
import webbrowser
import os

import fire


file_path = os.path.dirname(__file__) + "\\urls.json"


def main():
    fire.Fire()


def url(name):
    """指定のサイトに遷移する機能。"""
    urls_file = open(file_path)
    urls_dict = json.load(urls_file)
    for url_map in urls_dict:
        target_name = url_map["name"]
        if target_name == name:
            target_url = url_map["url"]
            webbrowser.open(target_url, new=0, autoraise=True)
            return

    return "指定されたサイトが存在しません。"


def add(name: str, url: str) -> str:
    """URLの追加を行う。"""
    file_path = os.path.dirname(__file__) + "\\urls.json"

    # ファイルが存在しない場合は新規作成
    if not os.path.exists(file_path):
        with open(file_path, 'w') as f:
            f.write("[]")

    # 読み込み
    with open(file_path, "r") as urls_file:
        urls_dict = json.load(urls_file)

        # サイト名が重複している場合はエラー
        for url_map in urls_dict:
            if url_map["name"] == name:
                return "サイト名が重複しています。別の名前で登録してください。"

        # URL形式の判定
        url_pattern = "https?://[\w/:%#\$&\?\(\)~\.=\+\-]+"
        if not re.match(url_pattern, url):
            return "URLの形式が間違っています。確認してください。"

        # 追加処理
        with open(file_path, "w") as write_file:
            urls_dict.append({"name": name, "url": url})
            json.dump(urls_dict, write_file, indent=4)

    return "追加完了"


def list():
    """URL一覧を確認する機能。"""
    try:
        with open(file_path) as urls_file:
            urls_dict = json.load(urls_file)
            for url_map in urls_dict:
                target_name = url_map["name"]
                target_url = url_map["url"]
                print(target_name, target_url)
    except FileNotFoundError:
        return "addコマンドで、URLを追加してください。"


def path():
    print(__file__)
    print(os.chdir(__file__))


if __name__ == "__main__":
    main()
