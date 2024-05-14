from tlib.core.cfg import Cfg
from typing import Optional
import os
from pathlib import Path
from tlib.ml.dataset import get_data_dir
from pexels_api import API as PexelAPI
from requests import get
import tqdm


class PexelDownloader:
    """Downloads images from Pexel through its API"""

    def __init__(self):
        env = os.environ["ENV"]
        cfg = Cfg(env)
        self.pexel_api = PexelAPI(cfg.get_api_conf_value("PEXELS", "APIKEY"))

    def download(
            self,
            dataset_name: str,
            category_name: Optional[str],
            keyword: str,
            page_st: int = 1,
            page_end: int = 2
    ) -> int:
        """
        Download images from Pexel and persists them to the specified dataset&category.
        Number of downloaded & persisted images are returned.
        """
        ml_data_path = get_data_dir()
        save_path = Path(ml_data_path).joinpath(dataset_name)

        if category_name is not None:
            save_path = save_path.joinpath(category_name)

        save_path.mkdir(parents=True, exist_ok=True)
        cnt = 0
        for page in tqdm.tqdm(range(page_st, page_end), desc = "Pexels Page"):
            rez = self.pexel_api.search(
                keyword, page=page, results_per_page=50)
            photos = rez["photos"]
            for photo in tqdm.tqdm(photos, desc = "Photos per page"):
                img_id = photo["id"]
                img_url = photo["src"]["medium"]
                resp = get(img_url)
                fname = f"{img_id}.jpg"
                self._persist(str(save_path.joinpath(fname)), resp.content)
                cnt += 1

        return cnt

    def _persist(self, fpath: str, content) -> None:
        """Persist image data to fpath"""
        with open(fpath, "wb") as fd:
            fd.write(content)
