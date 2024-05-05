from unittest import TestCase, main
from tlib.net.whois import *


class WhoisTest(TestCase):

    def test_whois_happycase(self):
        wr = whois("toyota.co.jp")
        print(wr)
        wr = whois("sony.co.jp")
        print(wr)


if __name__ == "__main__":
    main()
