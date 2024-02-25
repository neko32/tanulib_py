from unittest import TestCase, main
from tlib.sql import *
import sqlite3
import os


class SQLiteTest(TestCase):

    def quote_db_path(self, db_name: str) -> str:
        return f"{os.environ['HOME_DB_PATH']}/{db_name}"

    def test_createtbl_ins_sel(self):
        db_path = self.quote_db_path("tlibut.sqlite3")
        conn = sqlite3.connect(db_path)
        tbl_bld = TableBuilder(db_path, "NekoInfo")
        tbl_bld.add_col(
            name="id",
            ct_type=ColumnType.CT_TYPE_INT,
            is_primary_key=True,
            is_required=True
        )
        tbl_bld.add_col(
            name="name",
            ct_type=ColumnType.CT_TYPE_TEXT,
            is_primary_key=False,
            is_required=True
        )
        tbl_bld.add_col(
            name="age",
            ct_type=ColumnType.CT_TYPE_INT,
            is_primary_key=False,
            is_required=True
        )
        tbl_bld.add_col(
            name="hobby",
            ct_type=ColumnType.CT_TYPE_TEXT,
            is_primary_key=False,
            is_required=False,
            default_value="Playing with Toy"
        )

        self.assertTrue(
            tbl_bld.create(
                conn_to_use=conn,
                force_drop_existing_tbl=True,
                verbose=True
            )
        )

        data = [
            ("takori", 3),
            ("shima", 2),
            ("torachan", 17)
        ]

        ins_rez = insert_to_table(
            conn=conn,
            table_name="NekoInfo",
            col_names=['name', 'age'],
            recs=data,
            verbose=True
        )
        self.assertTrue(ins_rez)

        try:
            rez = conn.execute("select * from NekoInfo")
            fetched_rows = rez.fetchall()
            for nrow, r in enumerate(fetched_rows):
                if nrow == 0:
                    self.assertEqual(r[1], 'takori')
                    self.assertEqual(r[2], 3)
                    self.assertEqual(r[3], 'Playing with Toy')
                elif nrow == 1:
                    self.assertEqual(r[1], 'shima')
                    self.assertEqual(r[2], 2)
                    self.assertEqual(r[3], 'Playing with Toy')
                elif nrow == 2:
                    self.assertEqual(r[1], 'torachan')
                    self.assertEqual(r[2], 17)
                    self.assertEqual(r[3], 'Playing with Toy')
            self.assertEqual(len(fetched_rows), 3)
        except Exception as e:
            print(e)
            self.assertTrue(False)

        conn.close()


if __name__ == "__main__":
    main()
