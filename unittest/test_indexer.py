from unittest import TestCase, main
from pathlib import Path
from tlib.nlp.indexer import *


class IndexerTest(TestCase):
    csv_path = Path(__file__).parent.joinpath(
        "testdata", "csv", "test_ipt.csv")
    if not csv_path.exists():
        raise Exception(f"{str(csv_path)} doesn't exist")

    indexer = Indice(str(csv_path), 1)
    print(indexer.summary())


if __name__ == "__main__":
    main()
