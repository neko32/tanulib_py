import sqlite3
from typing import Optional, List
from pathlib import Path
import csv


class TableInfo:
    """
    Persists Table's metadata
    """

    def __init__(
        self,
        id: int,
        name: str,
        type_name: str,
        is_notnull: int,
        default_value: Optional[str],
        is_pk: int
    ):
        self._id = id
        self._name = name
        self._type_name = type_name
        self._is_notnull = True if is_notnull == 1 else False
        self._default_value = default_value
        self._is_pk = True if is_pk == 1 else False

    @property
    def id(self) -> int:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @property
    def type_name(self) -> str:
        return self._type_name

    @property
    def is_notnull(self) -> bool:
        return self._is_notnull

    @property
    def default_value(self) -> Optional[str]:
        return self.default_value

    @property
    def is_pk(self) -> bool:
        return self._is_pk

    def __str__(self) -> str:
        buf = "["
        buf += f"ID:{self._id},NAME:{self._name},"
        buf += f"TYPENAME:{self._type_name},IS_NOTNULL:{self._is_notnull},"
        buf += f"DEFAULT_VALUE:{self._default_value},IS_PK:{self._is_pk}]"
        return buf

    def __repr__(self) -> str:
        return self.__str__()


def get_table_info(
    db_path: str,
    table_name: str
) -> List[TableInfo]:
    """Get all table's info found in the db_path using PRAGMA table_info()"""
    conn = sqlite3.connect(db_path)
    try:
        cursor = conn.cursor()
        # parameter doesn't work for PRAGMA
        schema_info = cursor.execute(f"PRAGMA table_info({table_name})")
        rez = schema_info.fetchall()
        tblinfo = []

        for id, name, type_name, is_notnull, defv, is_pk in rez:
            tblinfo.append(
                TableInfo(id, name, type_name, is_notnull, defv, is_pk))
        cursor.close()
        conn.close()
        return tblinfo

    except Exception as e:
        print(e)
        raise e


def export_to_csv(
    db_path: str,
    table_name: str,
    file_loc: str
) -> None:
    """
    Export table's data as CSV format
    """
    path = Path(file_loc)
    if not path.parent.exists:
        raise f"{str(path.parent)} doesn't exist"
    conn = sqlite3.connect(db_path)
    try:
        cursor = conn.cursor()
        rc = cursor.execute(f"SELECT * from {table_name}")
        fetched_rows = rc.fetchall()

        with open(file_loc, "w") as fd:
            csv_w = csv.writer(fd)
            for _, r in enumerate(fetched_rows):
                csv_w.writerow(r)

        cursor.close()
        conn.close()

    except Exception as e:
        print(e)
        raise e
