from unittest import TestCase, main
from tlib.datautil.yaml import *
from tlib.testutil.file import get_tmp_dir
from pathlib import Path


class YamlTest(TestCase):

    def test_to_csv(self):
        yaml_path = str(Path(__file__).parent.joinpath(
            "testdata", "yaml", "sample_repeat_same.yaml"))
        tmp_yaml = Path(get_tmp_dir()).joinpath("yamltest.csv")

        if tmp_yaml.exists():
            tmp_yaml.unlink()

        to_csv(yaml_path, str(tmp_yaml), True)


if __name__ == "__main__":
    main()
