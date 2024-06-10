from tlib.office.ss_ops import *

def main():
    ods = SpreadSheetOps("sample_ss.ods", SpreadSheetFormat.ODS)
    print(f"num of sheets are {ods.get_num_sheets()}")
    ods.switch_sheet_view(0)

if __name__ == "__main__":
    main()
