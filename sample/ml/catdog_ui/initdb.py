from tlib.sql import TableBuilder, ColumnType, create_db
from argparse import ArgumentParser
import os
from pathlib import Path


def main(env:str):

    db_file_name = f"catdog_{env}.sqlite3"
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
    parser = ArgumentParser(
        prog = "initdb.py",
        usage = "python3 initdb.py {env}",
        description = "initialize db for catdog_ui",
    )
    parser.add_argument("-e", "--env", default = "local", choices = ["local", "dev", "qa", "staging", "prod"], required = True)
    args = parser.parse_args()
    env = args.env
    main(env)
