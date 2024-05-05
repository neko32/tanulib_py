import MeCab
from csv import writer

class Wakatigaki:
    """
    Provides Wakatigaki feature (word dividing) for Japanese sentences
    """

    def __init__(self):
        self.engine = MeCab.Tagger("-Owakati")
        self.buffer = ""

    def parse(self, s: str) -> str:
        """Do wakatigaki for Japanese sentences"""
        self.buffer = self.engine.parse(s).strip()
        return self.buffer

    def persist_as_csv(self, csv_path:str) -> None:
        """Persist result to csv"""

        if len(self.buffer) == 0:
            raise Exception("Buffer is empty.")
        
        with open(csv_path, 'w') as fd:
            csv_w = writer(fd)
            for w in self.buffer.split(" "):
                csv_w.writerow([w])
            