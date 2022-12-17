import unittest
import os

from app import add


class TestUrlManager(unittest.TestCase):
    def setUp(self):
        # テスト用のファイルを作成
        file_path = os.path.dirname(__file__) + "\\urls.json"
        with open(file_path, "w") as f:
            f.write('[{"name": "test", "url": "https://test.com"}]')

    def tearDown(self):
        # テスト用のファイルを削除
        file_path = os.path.dirname(__file__) + "\\urls.json"
        os.remove(file_path)

    def test_add_success(self):
        # 正常系
        result = add("test2", "https://test2.com")
        self.assertEqual(result, "追加完了")

    def test_add_name_duplicate(self):
        # 異常系
        result = add("test", "https://test2.com")
        self.assertEqual(result, "サイト名が重複しています。別の名前で登録してください。")

    def test_add_invalid_url(self):
        # 異常系
        result = add("test2", "test2.com")
        self.assertEqual(result, "URLの形式が間違っています。確認してください。")


if __name__ == "__main__":
    unittest.main()
