from unittest import TestCase, main
from tlib.datautil import *

class StringTest(TestCase):

    def test_capitalize(self):
        s1 = "tanuki"
        s2 = "Tanuki"
        s3 = "TANUKI"
        s4 = "tANUKi"
        expected = "Tanuki"
        self.assertEqual(capitalize(s1), expected)
        self.assertEqual(capitalize(s2), expected)
        self.assertEqual(capitalize(s3), expected)
        self.assertEqual(capitalize(s4), expected)
        self.assertEqual(capitalize("t"), "T")
        self.assertEqual(capitalize(""), "")

    def test_from_snake_to_pascal(self):
        s1 = "tanu_tanuki"
        s2 = "tanu_tanu_ki"
        s3 = "tanu"
        s4 = "tanu_TANUKI"
        self.assertEqual(from_snake_case_to_pascal_case(s1), "TanuTanuki")
        self.assertEqual(from_snake_case_to_pascal_case(s2), "TanuTanuKi")
        self.assertEqual(from_snake_case_to_pascal_case(s3), "Tanu")
        self.assertEqual(from_snake_case_to_pascal_case(s4), "TanuTanuki")
        self.assertEqual(from_snake_case_to_pascal_case(""), "")
        self.assertEqual(from_snake_case_to_pascal_case("t"), "T")

    def test_from_snake_to_camel(self):
        s1 = "tanu_tanuki"
        s2 = "Tanu_tanuki"
        s3 = "tanu_TANUKI"
        s4 = "TANU_tanuki"
        s5 = "tanu"
        s6 = "Tanu"
        self.assertEqual(from_snake_case_to_camel_case(s1), "tanuTanuki")
        self.assertEqual(from_snake_case_to_camel_case(s2), "TanuTanuki")
        self.assertEqual(from_snake_case_to_camel_case(s3), "tanuTanuki")
        self.assertEqual(from_snake_case_to_camel_case(s4), "TanuTanuki")
        self.assertEqual(from_snake_case_to_camel_case(s5), "tanu")
        self.assertEqual(from_snake_case_to_camel_case(s6), "Tanu")
        self.assertEqual(from_snake_case_to_camel_case(""), "")
        self.assertEqual(from_snake_case_to_camel_case("t"), "t")
        self.assertEqual(from_snake_case_to_camel_case("T"), "T")
        self.assertEqual(from_snake_case_to_camel_case("ta"), "ta")
        self.assertEqual(from_snake_case_to_camel_case("Ta"), "Ta")

    def test_snake_to_chain(self):
        s1 = "neko_tako"
        s2 = "nekotako"
        s3 = "neko_tako"
        s4 = "Neko_Tako"
        s5 = "NEKO_TAKO"
        self.assertEqual(from_snake_to_chain_case(s1), 'neko-tako')
        self.assertEqual(from_snake_to_chain_case(s2), 'nekotako')
        self.assertEqual(from_snake_to_chain_case(s3), 'neko-tako')
        self.assertEqual(from_snake_to_chain_case(s4), 'neko-tako')
        self.assertEqual(from_snake_to_chain_case(s5), 'neko-tako')

if __name__ == "__main__":
    main()