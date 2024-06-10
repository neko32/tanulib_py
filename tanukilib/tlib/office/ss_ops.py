from enum import Enum
import pyexcel as pe
from typing import Optional


class SpreadSheetFormat(Enum):
    EXCEL = "excel"
    ODS = "ods"


class SpreadSheetOps:

    def __init__(self, file_path: str, format: SpreadSheetFormat):
        self._file_path = file_path
        self._format = format
        self._data: pe.Book = pe.get_book(file_name=self._file_path)
        self.sheet_view_idx = 0
        self.sheet_view = self._data.sheet_by_index(self.sheet_view_idx)

    def switch_sheet_view(self, n: int) -> None:
        sheet_nums = len(self._data.sheet_names())
        if n < 0 or n >= sheet_nums:
            raise ValueError(
                f"sheet view index must be between 0 and {sheet_nums - 1}")
        self.sheet_view_idx = n
        self.sheet_view = self._data.sheet_by_index(self.sheet_view_idx)

    def find_first_empty_cell_in_col(
            self,
            col: str,
            row_st: int,
            row_end: int = 65535) -> Optional[int]:
        if row_st < 1 or row_end < 1:
            raise ValueError("row_idx must be begger than equal 1")
        row_idx = row_st
        while row_idx <= row_end:
            try:
                if self.sheet_view[self.quote_cell(col, row_idx)] == "":
                    return row_idx
            except IndexError:
                return row_idx
            row_idx += 1
        return None

    def gets(self, r: str, c: int) -> Optional[str]:
        try:
            return str(self.sheet_view[self.quote_cell(r, c)])
        except IndexError:
            return None

    def geti(self, r: str, c: int) -> Optional[int]:
        try:
            return int(self.sheet_view[self.quote_cell(r, c)])
        except IndexError:
            return None

    def quote_cell(self, r: str, c: int) -> str:
        return f"{r}{c}"

    def get_num_sheets(self) -> int:
        return len(self._data.sheet_names())
