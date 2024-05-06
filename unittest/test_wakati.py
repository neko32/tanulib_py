from unittest import TestCase, main
from tlib.nlp.wakati import *
from tlib.testutil.tempfile_mgr import *
from csv import reader


class WakatigakiTest(TestCase):

    def test_wakati(self):
        w = Wakatigaki()
        rez = w.parse("たぬきとねこが楽しく遊びましたとさ。")
        expected = "たぬき と ねこ が 楽しく 遊び まし た と さ 。"
        self.assertEqual(rez.strip(), expected)

        key = "WakatigakiTest_test_wakati"

        tm = TempFileNameManager()
        tf_path = tm.generate(key)
        w.persist_as_csv(tf_path)
        print(tf_path)

        with open(tf_path, "r") as fd:
            csv_r = reader(fd)
            for l in csv_r:
                print(l[0])

        tm.remove(key)


if __name__ == "__main__":
    main()
