import datetime
import re


class BloodTestReport:

    def __init__(
            self,
            name: str,
            report_name: str,
            report_date: datetime.datetime
    ):
        self.protein = None
        self.albumin = None
        self.globulin = None
        self.a_g_ratio = None
        self.AST = None
        self.ALT = None
        self.alk_phosphatase = None
        self.GGT = None
        self.bilirubin = None
        self.BUN = None
        self.creatinine = None
        self.SDMA = None
        self.bun_creat_ratio = None
        self.phosphorus = None
        self.glucose = None
        self.calcium = None
        self.magnesium = None
        self.sodium = None
        self.potassium = None
        self.na_k_ratio = None
        self.chloride = None
        self.cholesterol = None
        self.triglyceride = None
        self.amylase = None
        self.precision_psl = None
        self.cpk = None
        self.name = name
        self.report_date = report_date
        self.report_name = report_name

    def is_attrib_albumin(self, key: str) -> bool:
        return True if key in ["albumin"] else False

    def set_attrib(self, key: str, value_s: str) -> None:
        key = key.lower().strip()
        if self.is_attrib_albumin(key):
            self.albumin = float(value_s)

    def set_by_antech_br_report(self, report: str) -> None:
        for line in report.splitlines():
            match = re.match(r"^([a-zA-Z0-9]+) ([0-9.,]+).*$", line)
            if match:
                print(match.groups())
