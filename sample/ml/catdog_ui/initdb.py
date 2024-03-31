from tlib.sql import TableBuilder, ColumnType, create_db
import os
from pathlib import Path


def main():

    db_file_name = "catdog.sqlite3"
    db_path = Path(os.environ["HOME_DB_PATH"]).joinpath(db_file_name)
    builder = TableBuilder(str(db_path), "Prediction")

    create_db(str(db_path.joinpath(db_file_name)))

    builder.add_col("id", ColumnType.CT_TYPE_INT, True, True)
    builder.add_col("input_name", ColumnType.CT_TYPE_TEXT, False, True)
    builder.add_col("model_name", ColumnType.CT_TYPE_TEXT, False, True)
    builder.add_col("result_summary", ColumnType.CT_TYPE_TEXT, False, False)
    builder.add_col("result_path", ColumnType.CT_TYPE_TEXT, False, False)
    builder.add_col("created_at", ColumnType.CT_TYPE_TEXT, False, True)
    builder.create(verbose=True)

    print("done.")


if __name__ == "__main__":
    main()
