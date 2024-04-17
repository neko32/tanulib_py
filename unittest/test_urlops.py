from tlib.web.urlops import URL
from unittest import TestCase, main
from pathlib import Path
from os import remove
import os


class URLOpsTest(TestCase):

    def test_URL_noport_nopath_noquery(self):
        url_str = "https://tanuki.org"
        url = URL(url_str)
        self.assertEqual(url.scheme, "https")
        self.assertEqual(url.scheme_domain_port(), url_str)
        self.assertIsNone(url.path())
        self.assertIsNone(url.query())

        url_str2 = "https://tanuki.org/"
        url2 = URL(url_str2)
        self.assertEqual(url2.scheme, "https")
        self.assertEqual(url2.scheme_domain_port(), url_str)
        self.assertIsNone(url2.path())
        self.assertIsNone(url2.query())

    def test_URL_withport_nopath_noquery(self):
        url_str = "https://tanuki.org:3378"
        url = URL(url_str)
        self.assertEqual(url.scheme_domain_port(), url_str)
        self.assertIsNone(url.path())
        self.assertIsNone(url.query())

    def test_URL_withport_withpath_noquery(self):
        url_str = "https://tanuki.org:3378/takoya/nekoya"
        url = URL(url_str)
        self.assertEqual(url.scheme_domain_port(), "https://tanuki.org:3378")
        self.assertEqual(url.path(), ['takoya', 'nekoya'])
        self.assertIsNone(url.query())

    def test_URL_withport_withpath_withquery(self):
        url_str = "https://tanuki.org:3378/takoya/nekoya?q=32&msg=neko"
        url = URL(url_str)
        self.assertEqual(url.scheme_domain_port(), "https://tanuki.org:3378")
        self.assertEqual(url.path(), ['takoya', 'nekoya'])
        self.assertEqual(url.query(), {'q': '32', 'msg': "neko"})

    def test_URL_noport_withpath_withquery(self):
        url_str = "https://tanuki.org/takoya/nekoya?q=32&msg=neko"
        url = URL(url_str)
        self.assertEqual(url.scheme_domain_port(), "https://tanuki.org")
        self.assertEqual(url.path(), ['takoya', 'nekoya'])
        self.assertEqual(url.query(), {'q': '32', 'msg': "neko"})

    def test_text_remote_copy(self):

        url_text = "https://www.aozora.gr.jp/cards/001351/files/49202_33049.html"
        temp_dir = Path(os.environ["HOME_TMP_DIR"]).joinpath("textpage.html")
        if temp_dir.exists():
            remove(str(temp_dir))
        url = URL(url_text)
        try:
            url.copy(temp_dir)
            self.assertTrue(temp_dir.exists())
        except Exception as e:
            print(e)
            self.assertTrue(False)


    def test_bin_remote_copy(self):

        url_img = "https://www.aozora.gr.jp/images/top_logo.png"
        temp_dir = Path(os.environ["HOME_TMP_DIR"]).joinpath("remote_logo.png")
        if temp_dir.exists():
            remove(str(temp_dir))
        url = URL(url_img)
        try:
            url.copy(temp_dir)
            self.assertTrue(temp_dir.exists())
        except Exception as e:
            print(e)
            self.assertTrue(False)


if __name__ == "__main__":
    main()
