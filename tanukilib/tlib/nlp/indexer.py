from csv import reader
import numpy as np
from pathlib import Path


class Indice:
    """Build words indice (indice for words in both way)"""

    def __init__(
            self,
            word_data_csv_path: str,
            UNK_level: int = 0,
            neighbor_size: int = 5,
            seed: int = 12345,
            verbose: bool = False
    ):
        with open(word_data_csv_path, 'r') as fd:
            csvr = reader(fd)
            words_raw = [w for w in csvr]
        words_raw = np.array(words_raw)
        words_raw = words_raw[:, 0]
        words = sorted(list(set(words_raw)))
        self.words_len = len(words)
        cnt = np.zeros(len(words))

        word_indices = {word: idx for idx, word in enumerate(words)}

        for i in range(0, len(words_raw)):
            cnt[word_indices[words_raw[i]]] += 1

        self.words_unknown = []

        for i in range(0, len(words)):
            if UNK_level > 0 and cnt[i] <= UNK_level:
                self.words_unknown.append(words[i])
                words[i] = 'UNK'

        self.word_indices = {word: idx for idx, word in enumerate(words)}
        self.word_indices_rev = {idx: word for idx, word in enumerate(words)}
        self.UNK_level = UNK_level
        self.total_words = len(words)

        # next, build training data

        intermed_text = np.zeros((len(words_raw), 1), dtype=int)
        for i in range(len(words_raw)):
            if words_raw[i] in word_indices:
                intermed_text[i, 0] = word_indices[words_raw[i]]
            else:
                intermed_text[i, 0] = word_indices['UNK']

        if verbose:
            print(f"intermediary word data size - {intermed_text.shape}")

        data = []
        target = []
        len_seq = len(intermed_text) - neighbor_size

        for i in range(neighbor_size, len_seq):
            data.append(intermed_text[i])
            # before n from target word at i
            target.extend(intermed_text[i - neighbor_size:i])
            # after n from target word at i
            target.extend(intermed_text[i + 1:i + 1 + neighbor_size])

        x_train = np.array(data).reshape(len(data), 1)
        y_train = np.array(target).reshape(len(data), neighbor_size * 2)
        zipped = list(zip(x_train, y_train))
        np.random.seed(seed)
        np.random.shuffle(zipped)
        x_train, y_train = zip(*zipped)

        self.x_train = np.array(x_train).reshape(len(data), 1)
        self.y_train = np.array(y_train).reshape(len(data), neighbor_size * 2)
        self.seed = seed
        self.neighbor_size = neighbor_size

    def summary(self) -> str:
        """Get Summary of indexing done at constructor"""
        buf = "======= SUMMARY START =======\n"
        buf += f"number of total words:{self.total_words}\n"
        buf += f"size of raw words:{self.words_len}\n"
        buf += f"size of word_indices: {len(self.word_indices)}\n"
        buf += f"UNK level:{self.UNK_level}\n"
        buf += f"size of UNK words:{len(self.words_unknown)}\n"
        buf += f"UNK words:{self.words_unknown}\n"
        buf += f"neighbor size:{self.neighbor_size}\n"
        buf += f"seed:{self.seed}\n"
        buf += f"x_train shape:{self.x_train.shape}\n"
        buf += f"y_train shape:{self.y_train.shape}\n"
        buf += "======= SUMMARY END =======\n"
        return buf

    def dump_corpus(self, out_file_dir: str, name: str) -> None:
        """Dump the generated corpus to specified out file."""
        path = Path(out_file_dir)
        if not path.exists():
            raise Exception(f"{out_file_dir} doesn't exist")
        path_for_corpus = str(path.joinpath(f"{name}_corpus.txt"))
        path_for_corpus_rev = str(path.joinpath(f"{name}_corpus_rev.txt"))

        with open(path_for_corpus, "w") as fd:
            for w, idx in self.word_indices.items():
                fd.write(f"{w}:{idx}\n")
        with open(path_for_corpus_rev, "w") as fd:
            for idx, w in self.word_indices_rev.items():
                fd.write(f"{idx}:{w}\n")
