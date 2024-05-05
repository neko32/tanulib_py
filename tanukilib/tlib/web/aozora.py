from tlib.web.urlops import URL
from bs4 import BeautifulSoup


class AozoraExtractor:
    """Extracts content as text from Aozora Bunko"""

    def __init__(self, url: str):
        self.url = URL(url)
        if self.url.domain_port() != "www.aozora.gr.jp":
            raise Exception("URL specified is not valid Aozora bunko site")

    def extract(self, out_file: str) -> None:
        """
        Retrieve Aozora bunko data and extract content as text format.
        Then the extracted text is persisted to out_file.
        """
        resp = self.url.get_str_response("Shift_JIS")
        bs = BeautifulSoup(resp, 'html.parser')

        title = bs.find("title").get_text()
        body = bs.find("div", {"class": "main_text"}).get_text()
        print(f"{title}\n\n{body}")

        with open(out_file, "w") as fd:
            fd.write(f"{title}\n\n{body}")
            print(f"{out_file} is written.")
