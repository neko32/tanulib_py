from tlib.sql import TableBuilder, ColumnType, create_db
import os
from pathlib import Path


def main():

    db_file_name = "aozora.sqlite3"
    db_path = Path(os.environ["HOME_DB_PATH"]).joinpath(db_file_name)
    builder = TableBuilder(str(db_path), "AozoraBooks")

    create_db(str(db_path.joinpath(db_file_name)))

    builder.add_col("id", ColumnType.CT_TYPE_INT, True, True)
    builder.add_col("input_id", ColumnType.CT_TYPE_TEXT, False, True)
    builder.add_col("author_id", ColumnType.CT_TYPE_INT, False, True)
    builder.add_col("author_name_en", ColumnType.CT_TYPE_TEXT, False, True)
    builder.add_col("author_name_ja", ColumnType.CT_TYPE_TEXT, False, True)
    builder.add_col("card_id", ColumnType.CT_TYPE_INT, False, True)
    builder.add_col("link_id", ColumnType.CT_TYPE_INT, False, True)
    builder.add_col("title_en", ColumnType.CT_TYPE_TEXT, False, False)
    builder.add_col("title_ja", ColumnType.CT_TYPE_TEXT, False, False)
    builder.add_col("created_at", ColumnType.CT_TYPE_TEXT, False, True)
    builder.create(verbose=True)

    print("done.")


if __name__ == "__main__":
    main()
