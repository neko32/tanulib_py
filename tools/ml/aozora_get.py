import os
import sys
from tlib.web.aozora import *
from tlib.csv.csvops import CSVOps
from tlib.nlp.wakati import Wakatigaki
from tlib.sql.sqlite_ops import insert_to_table, current_datetime_as_str
from pathlib import Path
import sqlite3


def main():

    conf_path = Path(os.environ["TANULIB_CONF_DIR"]).joinpath(
        "tlib", "aozora_db", "aozora_input.csv")
    iptdb = CSVOps(conf_path, "id")

    target_id = "OG00002"

    ipts = iptdb.get_row_by_row_key(target_id)
    if ipts.size == 0:
        print(f"target_id {target_id} is not found.")
        sys.exit(1)

    base_url = "https://www.aozora.gr.jp/cards"
    author_id = int(ipts["author_id"])
    card_id = int(ipts["card_id"])
    link_id = int(ipts["link_id"])
    author_id_str = format(author_id, "06d")

    target = f"{author_id_str}/files/{card_id}_{link_id}.html"
    aozora_url = f"{base_url}/{target}"
    mldata_dir = Path(os.environ["TLIB_ML_DATA_DIR"])
    content_file_path = mldata_dir.joinpath(
        "aozora", "novels", f"{author_id}_{card_id}_{link_id}.txt")
    wakati_csv_path = mldata_dir.joinpath(
        "aozora", "novels", f"{author_id}_{card_id}_{link_id}.csv")

    out_content_file = str(content_file_path)
    out_wakati_file = str(wakati_csv_path)

    print(aozora_url)
    print(out_content_file)
    print(out_wakati_file)

    try:
        print("=== STEP1: Retrieve the book from Aozora Bunko")
        ao = AozoraExtractor(aozora_url)
        title_and_body = ao.extract(out_content_file)

        print("=== STEP1: DONE!")
        print("=== STEP2: Generate Wakatigaki file for the book")
        wak = Wakatigaki()
        wak.parse(title_and_body)
        wak.persist_as_csv(out_wakati_file)

        print("=== STEP2: DONE!")
        print("=== STEP3: Register the book and input id to the Aozora DB")
        insert_to_db(ipts, target_id)
        print("=== STEP3: DONE!")
        print("All steps done now.")
    except Exception as e:
        raise e


def insert_to_db(ipts, input_id) -> None:

    db_file_name = "aozora.sqlite3"
    db_path = Path(os.environ["HOME_DB_PATH"]).joinpath(db_file_name)

    conn = sqlite3.Connection(db_path)
    cur_time = current_datetime_as_str()
    col_names = [
        "author_id", "input_id", "author_name_en",
        "author_name_ja", "card_id", "link_id",
        "title_en", "title_ja", "created_at"
    ]
    vals = [
        [
            int(ipts["author_id"]), input_id, ipts["author_name_en"],
            ipts["author_name_ja"], int(ipts["card_id"]), int(ipts["link_id"]),
            ipts["title_en"], ipts["title_ja"], cur_time
        ]
    ]
    insert_to_table(
        conn=conn,
        col_names=col_names,
        table_name="AozoraBooks",
        recs=vals,
        verbose=True
    )
    conn.close()


if __name__ == "__main__":
    main()
