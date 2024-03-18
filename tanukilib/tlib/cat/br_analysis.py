import datetime
import re
import pandas as pd
from typing import List


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
        self.T4 = None
        self.WBC = None
        self.RBC = None
        self.HGB = None
        self.HCT = None
        self.MCV = None
        self.name = name
        self.report_date = report_date
        self.report_name = report_name

    def get_report_name_with_date_postfix(self) -> str:
        return f"{self.report_date.strftime('%Y%m%d')}_{self.report_name}"

    def get_attribs_as_list(self) -> List[float]:
        return [
            self.protein, self.albumin, self.globulin, self.a_g_ratio,
            self.AST, self.ALT, self.alk_phosphatase, self.GGT,
            self.bilirubin, self.BUN, self.creatinine, self.SDMA,
            self.bun_creat_ratio, self.phosphorus, self.glucose, self.calcium,
            self.magnesium, self.sodium, self.potassium,
            self.na_k_ratio, self.chloride, self.cholesterol, self.triglyceride,
            self.amylase, self.precision_psl, self.cpk,
            self.T4, self.WBC, self.RBC,
            self.HGB, self.HCT, self.MCV
        ]

    def is_attrib_protein(self, key: str) -> bool:
        return True if key in ["total_protein"] else False

    def is_attrib_albumin(self, key: str) -> bool:
        return True if key in ["albumin"] else False

    def is_attrib_globulin(self, key: str) -> bool:
        return True if key in ["globulin"] else False

    def is_attrib_bilirubin(self, key: str) -> bool:
        return True if key in ["total_bilirubin"] else False

    def is_attrib_agratio(self, key: str) -> bool:
        return True if key in ["a/g_ratio"] else False

    def is_attrib_bin_creat_ratio(self, key: str) -> bool:
        return True if key in ["bun/creat_ratio"] else False

    def is_attrib_na_k_ratio(self, key: str) -> bool:
        return True if key in ["na/k_ratio"] else False

    def is_attrib_ast(self, key: str) -> bool:
        return True if key in ["ast_sgot"] else False

    def is_attrib_alt(self, key: str) -> bool:
        return True if key in ["alt_sgpt"] else False

    def is_attrib_alk_phosphatase(self, key: str) -> bool:
        return True if key in ["alk_phosphatase"] else False

    def is_attrib_GGT(self, key: str) -> bool:
        return True if key in ["ggt"] else False

    def is_attrib_BUN(self, key: str) -> bool:
        return True if key in ["bun"] else False

    def is_attrib_creatinine(self, key: str) -> bool:
        return True if key in ["creatinine"] else False

    def is_attrib_SDMA(self, key: str) -> bool:
        return True if key in ["SDMA"] else False

    def is_attrib_phosphorus(self, key: str) -> bool:
        return True if key in ["phosphorus"] else False

    def is_attrib_glucose(self, key: str) -> bool:
        return True if key in ["glucose"] else False

    def is_attrib_calcium(self, key: str) -> bool:
        return True if key in ["calcium"] else False

    def is_attrib_magnesium(self, key: str) -> bool:
        return True if key in ["magnesium"] else False

    def is_attrib_sodium(self, key: str) -> bool:
        return True if key in ["sodium"] else False

    def is_attrib_potassium(self, key: str) -> bool:
        return True if key in ["potassium"] else False

    def is_attrib_chloride(self, key: str) -> bool:
        return True if key in ["chloride"] else False

    def is_attrib_cholesterol(self, key: str) -> bool:
        return True if key in ["cholesterol"] else False

    def is_attrib_amylase(self, key: str) -> bool:
        return True if key in ["amylase"] else False

    def is_attrib_precision_psl(self, key: str) -> bool:
        return True if key in ["precisionpsl"] else False

    def is_attrib_cpk(self, key: str) -> bool:
        return True if key in ["cpk"] else False

    def is_attrib_T4(self, key: str) -> bool:
        return True if key in ["t4"] else False

    def is_attrib_wbc(self, key: str) -> bool:
        return True if key in ["wbc"] else False

    def is_attrib_rbc(self, key: str) -> bool:
        return True if key in ["rbc"] else False

    def is_attrib_hgb(self, key: str) -> bool:
        return True if key in ["hgb"] else False

    def is_attrib_hct(self, key: str) -> bool:
        return True if key in ["hct"] else False

    def is_attrib_mcv(self, key: str) -> bool:
        return True if key in ["mcv"] else False

    def set_attrib(self, key: str, value_s: str) -> None:
        key = key.lower().strip()
        value_s = value_s.replace(",", "")
        if self.is_attrib_protein(key):
            self.protein = float(value_s)
        elif self.is_attrib_albumin(key):
            self.albumin = float(value_s)
        elif self.is_attrib_globulin(key):
            self.globulin = float(value_s)
        elif self.is_attrib_agratio(key):
            self.a_g_ratio = float(value_s)
        elif self.is_attrib_ast(key):
            self.AST = float(value_s)
        elif self.is_attrib_alt(key):
            self.ALT = float(value_s)
        elif self.is_attrib_alk_phosphatase(key):
            self.alk_phosphatase = float(value_s)
        elif self.is_attrib_GGT(key):
            self.GGT = float(value_s)
        elif self.is_attrib_bilirubin(key):
            self.bilirubin = float(value_s)
        elif self.is_attrib_BUN(key):
            self.BUN = float(value_s)
        elif self.is_attrib_creatinine(key):
            self.creatinine = float(value_s)
        elif self.is_attrib_SDMA(key):
            self.SDMA = float(value_s)
        elif self.is_attrib_bin_creat_ratio(key):
            self.bun_creat_ratio = float(value_s)
        elif self.is_attrib_phosphorus(key):
            self.phosphorus = float(value_s)
        elif self.is_attrib_glucose(key):
            self.glucose = float(value_s)
        elif self.is_attrib_calcium(key):
            self.calcium = float(value_s)
        elif self.is_attrib_magnesium(key):
            self.magnesium = float(value_s)
        elif self.is_attrib_sodium(key):
            self.sodium = float(value_s)
        elif self.is_attrib_potassium(key):
            self.potassium = float(value_s)
        elif self.is_attrib_na_k_ratio(key):
            self.na_k_ratio = float(value_s)
        elif self.is_attrib_chloride(key):
            self.chloride = float(value_s)
        elif self.is_attrib_cholesterol(key):
            self.cholesterol = float(value_s)
        elif self.is_attrib_amylase(key):
            self.amylase = float(value_s)
        elif self.is_attrib_precision_psl(key):
            self.precision_psl = float(value_s)
        elif self.is_attrib_cpk(key):
            self.cpk = float(value_s)
        elif self.is_attrib_T4(key):
            self.T4 = float(value_s)
        elif self.is_attrib_wbc(key):
            self.WBC = float(value_s)
        elif self.is_attrib_rbc(key):
            self.RBC = float(value_s)
        elif self.is_attrib_hgb(key):
            self.HGB = float(value_s)
        elif self.is_attrib_hct(key):
            self.HCT = float(value_s)
        elif self.is_attrib_mcv(key):
            self.MCV = float(value_s)

    def set_by_antech_br_report(self, report: str) -> None:
        h = {}
        for line in report.lower().splitlines():
            # special preprocessing
            if line.startswith("total protein"):
                line = line.replace("total protein", "total_protein")
            elif line.startswith("total bilirubin"):
                line = line.replace("total bilirubin", "total_bilirubin")
            elif line.startswith("alk phosphatase"):
                line = line.replace("alk phosphatase", "alk_phosphatase")
            elif line.startswith("ast (sgot)"):
                line = line.replace("ast (sgot)", "ast_sgot")
            elif line.startswith("alt (sgpt)"):
                line = line.replace("alt (sgpt)", "alt_sgpt")
            elif line.startswith("a/g ratio"):
                line = line.replace("a/g ratio", "a/g_ratio")
            elif line.startswith("bun/creat ratio"):
                line = line.replace("bun/creat ratio", "bun/creat_ratio")
            elif line.startswith("na/k ratio"):
                line = line.replace("na/k ratio", "na/k_ratio")

            match = re.match(r"^([a-z0-9/_]+) ([0-9.,]+).*$", line)
            if match:
                g = match.groups()
                h[g[0]] = g[1]

        for key, value in h.items():
            self.set_attrib(key, value)


def to_df(reports: List[BloodTestReport]) -> pd.DataFrame:
    idx = list(map(lambda r: r.get_report_name_with_date_postfix(), reports))
    columns = [
        "Total_Protein", "Albumin", "Globulin",
        "A/G_Ratio", "AST_SGOT", "ALT_SGPT",
        "ALK_Phosphatase", "GGT", "Total_Bilirubin", "BUN",
        "Creatinine", "SDMA", "BIN/Creat_Ratio", "Phosphorus", "Glucose",
        "Calcium", "Magnesium", "Sodium", "Potassium", "NA/K_Ratio",
        "Chloride", "Cholesterol", "Triglyceride", "Amylase",
        "PrecisionPSL", "CPK", "T4", "WBC", "RBC",
        "HGB", "HCT", "MCV"
    ]
    data = []
    for report in reports:
        data.append(report.get_attribs_as_list())
    return pd.DataFrame(
        data=data,
        columns=columns,
        index=idx
    )
