# 概要

Cli形式でチートシートを管理する。

## インストール方法

1. git cloneを行う。
2. トップディレクトリ(README.mdのあるディレクトリ)にてコマンドプロンプトを開く。
3. 以下のコマンドを実行する

```
install
```

insta.batが実行され、ます。

4. インストール完了。

## 利用している技術

- [python-fire](https://github.com/google/python-fire/blob/master/docs/guide.md)
- [python-inquirer](https://github.com/magmax/python-inquirer)

## コマンド一覧

```shell
cheat
```

cheatコマンドのみ打つと、コマンド一覧が表示されます。

一覧から抜けるには「q」を押してください。

## 機能

- cheat add <app_name> <command> <description>
  - example
    - cheat add vscode "ctrl c" "コピー"
- cheat list
- cheat delete <app_name>

## 開発用メモ

- 実行
  - python src/app.py add <APP> <COMMAND> <Description>
    - コマンド追加
  - python src/app.py list
    - リスト一覧

- テスト
  - python src/test_app.py