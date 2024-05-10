from unittest import TestCase, main
from tlib.datautil.yaml import *
from tlib.testutil.file import get_tmp_dir
from pathlib import Path
from csv import reader


class YamlTest(TestCase):

    def test_to_csv(self):
        yaml_path = str(Path(__file__).parent.joinpath(
            "testdata", "yaml", "sample_repeat_same.yaml"))
        tmp_yaml = Path(get_tmp_dir()).joinpath("yamltest.csv")

        if tmp_yaml.exists():
            tmp_yaml.unlink()

        to_csv(yaml_path, str(tmp_yaml), True)

        with open(str(tmp_yaml), "r") as fd:
            csvr = reader(fd)
            cnt = 0
            headers = [
                'key', 'title', 'author_name',
                'author_age', 'year', 'pages', 'chapters'
            ]
            for row in csvr:
                if cnt == 0:
                    self.assertListEqual(row, headers)
                if cnt == 1:
                    self.assertEqual(row[1], "Introduction to YAML")
                    self.assertEqual(row[3], '38')
                if cnt == 2:
                    self.assertEqual(row[1], "Tako to Neko")
                    self.assertEqual(row[3], '50')
                cnt += 1

            self.assertEqual(cnt, 3)

        if tmp_yaml.exists():
            tmp_yaml.unlink()


if __name__ == "__main__":
    main()
