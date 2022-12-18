# 概要

Cli形式でチートシートを管理する。

## インストール方法

1. git cloneを行う。
2. トップディレクトリ(README.mdのあるディレクトリ)にてコマンドプロンプトを開く。
3. 以下のコマンドを実行する

```cli
python setup.py install
```

4. コマンドプロンプト上で「bookmark url youtube」を打ち込み、Youtubeが開いたらインストール完了。

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

- cheat add <name> <url>
- cheat list

## 開発用メモ

- 実行
  - python src/app.py add <APP> <COMMAND>
    - コマンド追加
  - python src/app.py list
    - リスト一覧

- テスト
  - python src/test_app.py