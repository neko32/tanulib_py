from unittest import TestCase, main
from tlib.net.dns import *


class DNSTest(TestCase):

    def test_query_txt(self):
        q = DNSResolver("sony.co.jp", RDataType.TXT)
        q.query()
        print(q.txt)
        self.assertTrue(len(q.txt) > 0)

    def test_query_ns(self):
        q = DNSResolver("sony.co.jp", RDataType.NAMESERVER)
        q.query()
        self.assertTrue(len(q.nameservers) > 0)
        self.assertTrue(q.last_answer_size > 0)
        self.assertEqual(q.qname, "sony.co.jp.")


if __name__ == "__main__":
    main()
