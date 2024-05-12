from tlib.ml.word2vec import Word2Vec
from tlib.ml.dataset import get_data_dir
from pathlib import Path


def main():
    csv_file = str(Path(get_data_dir()).joinpath(
        "aozora", "novels", "2035_59517_67534.csv"))
    w2v = Word2Vec(csv_file, 10)
    w2v.build_model()
    w2v.fit(batch_size=200, epochs=100)


if __name__ == "__main__":
    main()
