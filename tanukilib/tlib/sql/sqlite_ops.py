import sqlite3
from enum import Enum
from typing import List, Any, Optional
from pathlib import Path
from tlib.core import exec_cmd
from tlib.dateutil.date_repr import cur_datetime_as_std_fmt_str


class ColumnType(Enum):
    """Enum to represent column type"""
    CT_TYPE_INT = "INTEGER"
    CT_TYPE_TEXT = "TEXT"
    CT_TYPE_REAL = "REAL"
    CT_TYPE_BLOB = "BLOB"
    CT_TYPE_NULL = "NULL"


class TableBuilder:
    """Build a table with specified meta data for the table"""

    def __init__(self, db_path: str, name: str) -> None:
        self.db_path = db_path
        self.name = name
        self.cols = []

    def add_col(
            self,
            name: str,
            ct_type: ColumnType,
            is_primary_key: bool,
            is_required: bool,
            default_value: Any = None
    ) -> None:
        """Add a column with given meta data"""
        self.cols.append(
            (
                name,
                ct_type,
                is_primary_key,
                is_required,
                default_value
            )
        )

    def create(
            self,
            conn_to_use: Optional[sqlite3.Connection] = None,
            force_drop_existing_tbl: bool = True,
            verbose: bool = False) -> bool:
        """Create the table with instructed data"""
        buf = f"CREATE TABLE IF NOT EXISTS {self.name} (\n"
        for idx, (c_name, c_type, cp, c_isreq, c_defv) in enumerate(self.cols):
            buf += f"  {c_name} {c_type.value} "
            if cp:
                buf += "PRIMARY KEY AUTOINCREMENT"
            else:
                if c_isreq:
                    buf += "NOT NULL "
                if c_defv is not None:
                    quote = '"' if c_type == ColumnType.CT_TYPE_TEXT else ''
                    buf += f'DEFAULT {quote}{c_defv}{quote} '

            buf = buf.rstrip()
            if idx == len(self.cols) - 1:
                buf += "\n"
            else:
                buf += ",\n"

        buf += ");\n"

        try:
            conn = sqlite3.connect(
                self.db_path) if conn_to_use is None else conn_to_use
            cur = conn.cursor()

            # drop table if force_drop_existing_tbl flag is set
            if force_drop_existing_tbl:
                if verbose:
                    print("dropping table {self.name} if exists..")
                cur.execute(f"DROP TABLE IF EXISTS {self.name};")
                conn.commit()
                if verbose:
                    print("dropping existing table done.")

            # run DDL
            if verbose:
                print("running the generated DDL:")
                print(buf)
            cur.execute(buf)
            conn.commit()
            if verbose:
                print(f"creating table {self.name} to {self.db_path} is done.")

            cur.close()
            if conn_to_use is None:
                conn.close()

            return True

        except Exception as e:
            print(e)
            return False


def insert_to_table(
        conn: sqlite3.Connection,
        table_name: str,
        col_names: List[str],
        recs: List[List[Any]],
        verbose: bool = False
) -> bool:
    """Insert records to the table"""
    values = ','.join(['?'] * len(recs[0]))
    buf = f"insert into {table_name} ({','.join(col_names)}) values({values})"

    try:
        if verbose:
            print("inserting rec(s) - running the below query:")
            print(buf)
        cursor = conn.cursor()
        cursor.executemany(buf, recs)
        conn.commit()
        cursor.close()
        if verbose:
            print("inserting rec(s) done.")
        return True
    except Exception as e:
        print(e)
        return False


def update_table(
        conn: sqlite3.Connection,
        table_name: str,
        col_names: List[str],
        upd_values: List[Any],
        where_col_names: Optional[List[str]],
        where_vals: List[Any],
        verbose: bool = False
) -> bool:
    """
    Update existing records with given condition
    """
    buf = f"UPDATE {table_name} SET "
    for col_name in col_names:
        buf += f"{col_name}=?,"
    buf = buf[:-1]

    if where_col_names is not None:
        buf += " WHERE "
        for col_name in where_col_names:
            buf += f"{col_name}=? AND "
        buf = buf[:-5]

    vals_param = tuple(upd_values + where_vals)

    try:
        if verbose:
            print("updating rec(s) - running the below query:")
            print(buf)
            print(f"params to supply - {vals_param}")
        cursor = conn.cursor()
        cursor.executemany(buf, [vals_param])
        conn.commit()
        cursor.close()
        if verbose:
            print("updating rec(s) done.")
        return True
    except Exception as e:
        print(e)
        return False


def delete_from_table(
    conn: sqlite3.Connection,
    table_name: str,
    col_names: Optional[List[str]] = None,
    col_vals: Optional[List[Any]] = None,
    verbose: bool = False
) -> bool:
    """Delete records from the table when records match with given col name and values"""
    buf = f"DELETE FROM {table_name}"

    if col_names is not None:
        buf += " WHERE "
        for col_name in col_names:
            buf += f"{col_name}=? AND "
        buf = buf[:-5]

    try:
        if verbose:
            print("deleting rec(s) - running the below query:")
            print(buf)
            print(f"params to supply - {col_vals}")
        cursor = conn.cursor()
        cursor.executemany(buf, [col_vals])
        conn.commit()
        cursor.close()
        if verbose:
            print("deleting rec(s) done.")
        return True
    except Exception as e:
        print(e)
        return False


def drop_table(
    conn: sqlite3.Connection,
    table_name: str,
    verbose: bool = False
) -> bool:
    """Drop the table"""
    try:
        if verbose:
            print(f"droping table {table_name} .. ")
        cursor = conn.cursor()
        cursor.execute(f"drop table if exists {table_name}")
        conn.commit()
        cursor.close()
        if verbose:
            print(f"table {table_name} was dropped.")
        return True
    except Exception as e:
        print(e)
        return False


def create_db(path: str) -> bool:
    """Create an empty SQLite database file"""
    dbpath = Path(path)
    if dbpath.exists():
        return True

    rez, _, _ = exec_cmd(["sqlite3", str(dbpath), "\"VACUUM;\""])
    return rez == 1


def current_datetime_as_str() -> str:
    """An util function to get datetime string representation"""
    return cur_datetime_as_std_fmt_str(with_ssec=True)
