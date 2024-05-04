from unittest import TestCase, main
from tlib.net.dns import *
from dns.resolver import NoAnswer


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

    def test_query_addr(self):
        q = DNSResolver("sony.co.jp", RDataType.ADDRESS)
        q.query(verbose=True)
        self.assertTrue(len(q.addresses) > 0)
        self.assertTrue(q.last_answer_size > 0)
        self.assertEqual(q.qname, "sony.co.jp.")

    def test_query_addrv6(self):
        q = DNSResolver("google.com", RDataType.IPV6_ADDRESS)
        q.query(verbose=True)
        self.assertTrue(len(q.addresses_v6) > 0)
        self.assertTrue(q.last_answer_size > 0)
        self.assertEqual(q.qname, "google.com.")

    def test_query_cname(self):
        q = DNSResolver("www.sony.co.jp", RDataType.CNAME)
        q.query(verbose=True)
        self.assertTrue(len(q.canonical_names) > 0)
        self.assertTrue(q.last_answer_size > 0)
        self.assertEqual(q.qname, "www.sony.co.jp.")

    def test_query_hinfo(self):
        # nowadays none of DNS servers support HINFO
        with self.assertRaises(NoAnswer):
            q = DNSResolver("sony.co.jp", RDataType.HOST_INFO)
            q.query(verbose=True)


if __name__ == "__main__":
    main()
