from csv import reader
import numpy as np

class Indice:
    """Build words indice (indice for words in both way)"""

    def __init__(self, word_data_csv_path:str, UNK_level:int = 0):
        with open(word_data_csv_path, 'r') as fd:
            csvr = reader(fd)
            words_raw = [w for w in csvr]
        words_raw = np.array(words_raw)
        words_raw = words_raw[:,0]
        words = sorted(list(set(words_raw)))
        cnt = np.zeros(len(words))

        word_indices = {word:idx for idx, word in enumerate(words)}

        for i in range(0, len(words_raw)):
            cnt[word_indices[words_raw[i]]] += 1
        
        self.words_unknown = []

        for i in range(0, len(words)):
            if UNK_level > 0 and cnt[i] <= UNK_level:
                self.words_unknown.append(words[i])
                words[i] = 'UNK'

        self.word_indices = {word:idx for idx, word in enumerate(words)}
        self.word_indices_rev = {idx:word for idx, word in enumerate(words)}
        self.UNK_level = UNK_level
        self.total_words = len(words)
        
    def summary(self) -> str:
        """Get Summary of indexing done at constructor"""
        buf = "======= SUMMARY START =======\n"
        buf += f"number of total words:{self.total_words}\n"
        buf += f"size of word_indices: {len(self.word_indices)}\n"
        buf += f"UNK level:{self.UNK_level}\n"
        buf += f"size of UNK words:{len(self.words_unknown)}\n"
        buf += f"UNK words:{self.words_unknown}\n"
        buf += "======= SUMMARY END =======\n"
        return buf

        





