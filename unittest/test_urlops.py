from tlib.web.urlops import URL
from unittest import TestCase, main


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


if __name__ == "__main__":
    main()
