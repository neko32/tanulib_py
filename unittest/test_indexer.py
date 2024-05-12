from unittest import TestCase, main
from pathlib import Path
from tlib.nlp.indexer import *
from tlib.testutil.file import get_tmp_dir


class IndexerTest(TestCase):

    def test_index(self):

        out_path = get_tmp_dir()
        csv_path = Path(__file__).parent.joinpath(
            "testdata", "csv", "test_ipt.csv")
        if not csv_path.exists():
            raise Exception(f"{str(csv_path)} doesn't exist")

        indexer = Indice(str(csv_path), 1)
        print(indexer.summary())

        try:
            indexer.dump_corpus(out_path, "testcorpus")
        except Exception as e:
            print(e)
            self.fail(str(e))


if __name__ == "__main__":
    main()
