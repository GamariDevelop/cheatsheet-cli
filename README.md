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


## 機能

- bookmark list
  - 登録したBookmarkのurl一覧を表示。
- bookmark add <name> <url>
  - nameにurlを紐づけ、urlコマンドで呼び出せるようになる。
- bookmark url <name>
  - nameに紐付けられたurlのサイトを呼び出す。

## 使用例

## 開発用メモ

- テスト
  - python src/test_app.py