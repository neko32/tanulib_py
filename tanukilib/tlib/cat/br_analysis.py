import datetime
import re
import pandas as pd
from typing import List


class BloodTestReport:
    """
    Manages blood test report parsing and persist each data.
    """

    def __init__(
            self,
            name: str,
            report_name: str,
            report_date: datetime.datetime
    ):
        """
        Constructor. report name and report date will be used as index
        when the report data is converted as Panda's DataFrame.
        """
        self.protein = None
        """
        Total protein (TP). Albulin + Globulin
        """
        self.albumin = None
        """
        One of proteins.
        Albumin helps to transmit metabolites and
        nutorition and manage osmotic pressure.
        too low .. potential labor issue, malnutrition
        too high .. dehydration
        """
        self.globulin = None
        """
        One of proteins. TP - albumin.
        too low .. ulcer, potential labor issue
        too high .. inflamation, FIP, potential lymph issue
        """
        self.a_g_ratio = None
        """
        Albumin / Globulin ratio.
        """
        self.AST = None
        """
        An encyme contained by cells in labor, mustle and red corpuscles.
        AST high indicates some damage in either labor and/or mustle and/or red corpuscles
        """
        self.ALT = None
        """
        An encyme contained by cells in labor.
        ALT high indicates some damage in labor.
        """
        self.alk_phosphatase = None
        """
        An encyme created in labor, bone, kidney, and intestine.
        In healthy condition ALKP is discharged.
        But if not, ALKP seeps into blood
        """
        self.GGT = None
        """
        Gamma Grutamin Transferase.
        Mainly indicates labor but can be affected by others like
        diabetes, some malfunction in gallbladder
        """
        self.bilirubin = None
        """
        aka T-Bill. A hint for jaundice, labor issue, side effect from medicine
        """
        self.BUN = None
        """
        Urea nitrogen within blood.
        with healthy kidney, area is filtered properly and discharged.
        However, BUN becomes high too late - until kidney loses 75% of its function,
        BUN won't be increased. Instead check SDMA too.
        too low .. labor issue, low-protein food, anorexia,
        too high .. high-protein food, kidney issue, dehydration, steroid etc,.
        """
        self.creatinine = None
        """
        A metabolic decomposition product after using mustle and energy consumption.
        If cat has more mustles, it can be higher creatinine.
        Also it can be high due to dehydration.
        Otherwise it's a sign of kidney issue.
        Just like BUN, if creatinine is increased due to a genuine kidney issue,
        it means already majority of kidney function has been lost.
        Low creatinine is usually not an issue but a hint cat lacks mustle.
        """
        self.SDMA = None
        """
        SDMA is another hint for kidney issue.
        But in different with creatinine and BUN, SDMA can give a signal of
        potential kidney issue much earlier than BUN and creatinine.
        In addition, compared to creatinine, it will have no noise impact by mustle mass.
        """
        self.bun_creat_ratio = None
        """
        BUN/Creatinine ratio
        """
        self.phosphorus = None
        """
        amount of phosphate in blood.
        too low .. hyperparathyroidism
        too high .. hypoparathyroidism, disorders of blood vessels or heart, Vitamin D overdose
        """
        self.glucose = None
        """
        Glucose is digested as a source of energy.
        Extra glucose is stored as a gricogen in muscles or fat.
        High value is a hint of diabetes
        Too value is a hint of intake of xylitol or labor issue, ulcers
        """
        self.calcium = None
        """
        too high .. cancers, kidney issue, vitamin D overdose
        """
        self.magnesium = None
        """
        too low .. discharged by kidney, malfunction in digestive canal
        too high .. kidney issue
        """
        self.sodium = None
        """
        Natrium. Right amount of sodium is important
        to maintain osmotic pressue, tranmissions to mustles etc,.
        """
        self.potassium = None
        """
        Kalium (Potash). Right amount of sodium is important
        to maintain osmotic pressue, tranmissions to mustles etc,.
        """
        self.na_k_ratio = None
        """
        Natlium/Karium ratio
        """
        self.chloride = None
        """
        One of electrolytes in blood.
        Hint to electrolyte imbalance.
        """
        self.cholesterol = None
        """
        too low .. Hyperparathyroidism, numtrition problem
        too high .. kidney issue, diabetes, obesity
        """
        self.triglyceride = None
        """
        It can be used to indicate arteriosclerosis along with cholesterol.
        But this value can be affected by diet
        """
        self.amylase = None
        """
        Amylase can be a hint for potential pancreas issue.
        Gastroenteritis may cause increase.
        Steroid may decase amylase.
        e.g.
        """
        self.precision_psl = None
        """
        Pancreas-Specific-Lipase may indicate pancreas issues.
        """
        self.cpk = None
        """
        Creatine phosphokinase may indicate malfunction in mustle, heart and nerves nerves.
        However only CPK shouldn't be used for diagnosis.
        """
        self.T4 = None
        """
        A hormone secreted by thyroid.
        High T4 indicates hyperparathyroidism.
        Low T4 indicates hypoparathyroidism.
        """
        self.WBC = None
        """
        Number of white blood corpuscle.
        too high .. inflamation, stress, hyperparathyroidism, cancer
        too low .. virus
        """
        self.RBC = None
        """
        Number of red blood corpuscle.
        too high .. hyperparathyroidism, dehydration, heat/lang issue
        too low .. nutrituion issue, kidney or labor issue
        """
        self.HGB = None
        """
        Haemoglobin (HGB).
        Too high indicates dehydration and too low indicates anemia.
        """
        self.HCT = None
        """
        Percentage of red blood corpuscle in blood.
        Too high indicates dehydration and too low indicates anemia.
        """
        self.MCV = None
        """
        Indicates size of each red blood corpuscle.
        Too high .. hemolytic anemia
        Too low .. anesia due to lack of iron, inflamation, kidney issue
        """
        self.MCH = None
        """
        Indicates average amount of haemoglobin in each red blood corpuscle.
        MCH decrease before MCV decreases.
        """
        self.MCHC = None
        """
        Indicates density of haemoglobin in each red blood corpuscle.
        31~35 .. hypochromic
        <= 30 .. normochromic
        """
        self.platelet_count = None
        """
        Count of platelet. Impacts to stop bleeding.
        """
        self.neutrophils = None
        """
        Num of neutrophils.
        Increased number may indicate some injury or tumor.
        But it could be a high stress.
        Decreased number may indicate leukemia.
        """
        self.bands = None
        """
        bands
        """
        self.lymphocytes = None
        """
        Lymphocytes in white blood corpuscle.
        too low .. virus, stress, etc,.
        too high .. leukemia, after vaccine
        """
        self.monocytes = None
        """
        Monocytes takes only approx 2% in WBC.
        Increasing num might indicate virus, tumor, stress etc,.
        """
        self.eosinophils = None
        """
        Eosinophils takes only 4~6% in WBC.
        Increasing number may indicate rice, cancer or lung-releated issue
        """
        self.basophils = None
        """
        Basophils.
        """
        self.freet4_equilibrium_dialysis = None
        """
        See T4
        """
        self.tsh = None
        """
        Thyroid-Stimulating Hormone.
        """
        self.specific_gravity = None
        """
        Specific Gravity indicates health indicator for kidney.
        Low specific gravity indicates weak urine.
        """
        self.ph = None
        """
        Urine's PH
        1~6 .. acidic
        7~8 .. normal
        8~14 .. alkaline
        Alkaline condition may cause inflammation of urinary bladder
        """

        self.microalbuminuria = None
        """
        Micro amount of alubumin in urine
        """

        self.name = name
        """
        Name for a cat
        """
        self.report_date = report_date
        """
        Date for this report. This will be used for index in DF
        """
        self.report_name = report_name
        """
        Name for this report. This will be used for index in DF
        """

    def get_report_name_with_date_postfix(self) -> str:
        """
        get report name followed by a postfix with date.
        report name and report date are to be provided at constructor.
        """
        return f"{self.report_date.strftime('%Y%m%d')}_{self.report_name}"

    def get_attribs_as_list(self) -> List[float]:
        """
        get all attributes as list
        """
        return [
            self.protein, self.albumin, self.globulin, self.a_g_ratio,
            self.AST, self.ALT, self.alk_phosphatase, self.GGT,
            self.bilirubin, self.BUN, self.creatinine, self.SDMA,
            self.bun_creat_ratio, self.phosphorus, self.glucose, self.calcium,
            self.magnesium, self.sodium, self.potassium,
            self.na_k_ratio, self.chloride, self.cholesterol, self.triglyceride,
            self.amylase, self.precision_psl, self.cpk,
            self.T4, self.WBC, self.RBC,
            self.HGB, self.HCT, self.MCV,
            self.MCH, self.MCHC, self.platelet_count,
            self.neutrophils, self.bands, self.lymphocytes,
            self.monocytes, self.eosinophils, self.basophils,
            self.freet4_equilibrium_dialysis, self.tsh,
            self.specific_gravity, self.ph, self.microalbuminuria
        ]

    def is_attrib_protein(self, key: str) -> bool:
        """
        validate if an attribute is classified as protein
        """
        return True if key in ["total_protein"] else False

    def is_attrib_albumin(self, key: str) -> bool:
        """
        validate if an attribute is classified as albumin
        """
        return True if key in ["albumin"] else False

    def is_attrib_globulin(self, key: str) -> bool:
        """
        validate if an attribute is classified as globulin
        """
        return True if key in ["globulin"] else False

    def is_attrib_bilirubin(self, key: str) -> bool:
        """
        validate if an attribute is classified as bilirubin
        """
        return True if key in ["total_bilirubin"] else False

    def is_attrib_agratio(self, key: str) -> bool:
        """
        validate if an attribute is classified as A/G ratio
        """
        return True if key in ["a/g_ratio"] else False

    def is_attrib_bin_creat_ratio(self, key: str) -> bool:
        """
        validate if an attribute is classified as BIN/Creat ratio
        """
        return True if key in ["bun/creat_ratio"] else False

    def is_attrib_na_k_ratio(self, key: str) -> bool:
        """
        validate if an attribute is classified as NA/K ratio
        """
        return True if key in ["na/k_ratio"] else False

    def is_attrib_ast(self, key: str) -> bool:
        """
        validate if an attribute is classified as AST (SGOT)
        """
        return True if key in ["ast_sgot"] else False

    def is_attrib_alt(self, key: str) -> bool:
        """
        validate if an attribute is classified as ALT (SGPT)
        """
        return True if key in ["alt_sgpt"] else False

    def is_attrib_alk_phosphatase(self, key: str) -> bool:
        """
        validate if an attribute is classified as ALK Phosphatase
        """
        return True if key in ["alk_phosphatase"] else False

    def is_attrib_GGT(self, key: str) -> bool:
        """
        validate if an attribute is classified as GGT
        """
        return True if key in ["ggt"] else False

    def is_attrib_BUN(self, key: str) -> bool:
        """
        validate if an attribute is classified as BUN
        """
        return True if key in ["bun"] else False

    def is_attrib_creatinine(self, key: str) -> bool:
        """
        validate if an attribute is classified as Creatinine
        """
        return True if key in ["creatinine"] else False

    def is_attrib_SDMA(self, key: str) -> bool:
        """
        validate if an attribute is classified as SDMA
        """
        return True if key in ["sdma"] else False

    def is_attrib_phosphorus(self, key: str) -> bool:
        """
        validate if an attribute is classified as phosphorus
        """
        return True if key in ["phosphorus"] else False

    def is_attrib_glucose(self, key: str) -> bool:
        """
        validate if an attribute is classified as Glucose
        """
        return True if key in ["glucose"] else False

    def is_attrib_triglyceride(self, key: str) -> bool:
        """
        validate if an attribute is classified as triglyceride
        """
        return True if key in ["triglyceride"] else False

    def is_attrib_calcium(self, key: str) -> bool:
        """
        validate if an attribute is classified as calcium
        """
        return True if key in ["calcium"] else False

    def is_attrib_magnesium(self, key: str) -> bool:
        """
        validate if an attribute is classified as magnesium
        """
        return True if key in ["magnesium"] else False

    def is_attrib_sodium(self, key: str) -> bool:
        """
        validate if an attribute is classified as sodium
        """
        return True if key in ["sodium"] else False

    def is_attrib_potassium(self, key: str) -> bool:
        """
        validate if an attribute is classified as potassium
        """
        return True if key in ["potassium"] else False

    def is_attrib_chloride(self, key: str) -> bool:
        """
        validate if an attribute is classified as chloride
        """
        return True if key in ["chloride"] else False

    def is_attrib_cholesterol(self, key: str) -> bool:
        """
        validate if an attribute is classified as cholesterol
        """
        return True if key in ["cholesterol"] else False

    def is_attrib_amylase(self, key: str) -> bool:
        """
        validate if an attribute is classified as amylase
        """
        return True if key in ["amylase"] else False

    def is_attrib_precision_psl(self, key: str) -> bool:
        """
        validate if an attribute is classified as Precision PSL
        """
        return True if key in ["precisionpsl"] else False

    def is_attrib_cpk(self, key: str) -> bool:
        """
        validate if an attribute is classified as CPK
        """
        return True if key in ["cpk"] else False

    def is_attrib_T4(self, key: str) -> bool:
        """
        validate if an attribute is classified as T4
        """
        return True if key in ["t4"] else False

    def is_attrib_wbc(self, key: str) -> bool:
        """
        validate if an attribute is classified as WBC
        """
        return True if key in ["wbc"] else False

    def is_attrib_rbc(self, key: str) -> bool:
        """
        validate if an attribute is classified as RBC
        """
        return True if key in ["rbc"] else False

    def is_attrib_hgb(self, key: str) -> bool:
        """
        validate if an attribute is classified as HGB
        """
        return True if key in ["hgb"] else False

    def is_attrib_hct(self, key: str) -> bool:
        """
        validate if an attribute is classified as HCT
        """
        return True if key in ["hct"] else False

    def is_attrib_mcv(self, key: str) -> bool:
        """
        validate if an attribute is classified as MCV
        """
        return True if key in ["mcv"] else False

    def is_attrib_mch(self, key: str) -> bool:
        """
        validate if an attribute is classified as MCH
        """
        return True if key in ["mch"] else False

    def is_attrib_mchc(self, key: str) -> bool:
        """
        validate if an attribute is classified as MCHC
        """
        return True if key in ["mchc"] else False

    def is_attrib_platelet_count(self, key: str) -> bool:
        """
        validate if an attribute is classified as platelet count
        """
        return True if key in ["platelet_count"] else False

    def is_attrib_neutrophils(self, key: str) -> bool:
        """
        validate if an attribute is classified as neutrophils
        """
        return True if key in ["neutrophils"] else False

    def is_attrib_bands(self, key: str) -> bool:
        """
        validate if an attribute is classified as bands
        """
        return True if key in ["bands"] else False

    def is_attrib_lymphocytes(self, key: str) -> bool:
        """
        validate if an attribute is classified as lymphocytes
        """
        return True if key in ["lymphocytes"] else False

    def is_attrib_monocytes(self, key: str) -> bool:
        """
        validate if an attribute is classified as monocytes
        """
        return True if key in ["monocytes"] else False

    def is_attrib_eosinophils(self, key: str) -> bool:
        """
        validate if an attribute is classified as Eosinophils
        """
        return True if key in ["eosinophils"] else False

    def is_attrib_basophils(self, key: str) -> bool:
        """
        validate if an attribute is classified as basophils
        """
        return True if key in ["basophils"] else False

    def is_attrib_freet4_equilibrium_dialysis(self, key: str) -> bool:
        """
        validate if an attribute is classified as Free T4 by Equilibrium Dialysis
        """
        return True if key in ["freet4_equilibrium_dialysis"] else False

    def is_attrib_tsh(self, key: str) -> bool:
        """
        validate if an attribute is classified as TSH
        """
        return True if key in ["tsh"] else False

    def is_attrib_specific_gravity(self, key: str) -> bool:
        """
        validate if an attribute is classified as specific gravity
        """
        return True if key in ["specific_gravity"] else False

    def is_attrib_ph(self, key: str) -> bool:
        """
        validate if an attribute is classified as PH
        """
        return True if key in ["ph"] else False

    def is_attrib_microalbuminuria(self, key: str) -> bool:
        """
        validate if an attribute is classified as Microalbuminuria
        """
        return True if key in ["microalbuminuria"] else False

    def set_attrib(self, key: str, value_s: str) -> None:
        """
        set attribute by checking given key.
        If the given key is not caught by any attribute classifier,
        then the value provided is not stored.
        """
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
        elif self.is_attrib_triglyceride(key):
            self.triglyceride = float(value_s)
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
        elif self.is_attrib_mch(key):
            self.MCH = float(value_s)
        elif self.is_attrib_mchc(key):
            self.MCHC = float(value_s)
        elif self.is_attrib_platelet_count(key):
            self.platelet_count = float(value_s)
        elif self.is_attrib_neutrophils(key):
            self.neutrophils = float(value_s)
        elif self.is_attrib_bands(key):
            self.bands = float(value_s)
        elif self.is_attrib_lymphocytes(key):
            self.lymphocytes = float(value_s)
        elif self.is_attrib_monocytes(key):
            self.monocytes = float(value_s)
        elif self.is_attrib_eosinophils(key):
            self.eosinophils = float(value_s)
        elif self.is_attrib_basophils(key):
            self.basophils = float(value_s)
        elif self.is_attrib_freet4_equilibrium_dialysis(key):
            self.freet4_equilibrium_dialysis = float(value_s)
        elif self.is_attrib_tsh(key):
            self.tsh = float(value_s)
        elif self.is_attrib_specific_gravity(key):
            self.specific_gravity = float(value_s)
        elif self.is_attrib_ph(key):
            self.ph = float(value_s)
        elif self.is_attrib_microalbuminuria(key):
            self.microalbuminuria = float(value_s)

    def set_by_antech_br_report(self, report: str) -> None:
        """
        parse and set attribute the blood test report with Antech's format
        """
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
            elif line.startswith("platelet count"):
                line = line.replace("platelet count", "platelet_count")
            elif line.startswith("free t4 equilibrium dialysis"):
                line = line.replace(
                    "free t4 equilibrium dialysis", "freet4_equilibrium_dialysis")
            elif line.startswith("specific gravity"):
                line = line.replace("specific gravity", "specific_gravity")

            match = re.match(r"^([a-z0-9/_]+) ([0-9.,]+).*$", line)
            if match:
                g = match.groups()
                h[g[0]] = g[1]

        for key, value in h.items():
            self.set_attrib(key, value)


def to_df(reports: List[BloodTestReport]) -> pd.DataFrame:
    """
    return persisted attributes as Panda's DataFrame
    """
    idx = list(map(lambda r: r.get_report_name_with_date_postfix(), reports))
    columns = [
        "Total_Protein", "Albumin", "Globulin",
        "A/G_Ratio", "AST_SGOT", "ALT_SGPT",
        "ALK_Phosphatase", "GGT", "Total_Bilirubin", "BUN",
        "Creatinine", "SDMA", "BIN/Creat_Ratio", "Phosphorus", "Glucose",
        "Calcium", "Magnesium", "Sodium", "Potassium", "NA/K_Ratio",
        "Chloride", "Cholesterol", "Triglyceride", "Amylase",
        "PrecisionPSL", "CPK", "T4", "WBC", "RBC",
        "HGB", "HCT", "MCV", "MCH", "MCHC", "Platelet_Count",
        "Neutrophils", "Bands", "Lymphocytes", "Monocytes",
        "Eosinophils", "Basophils", "Free_T4_By_Equilibrium_Dialysis",
        "TSH", "Specific Gravity", "PH", "Microalbuminuria"
    ]
    data = []
    for report in reports:
        data.append(report.get_attribs_as_list())
    return pd.DataFrame(
        data=data,
        columns=columns,
        index=idx
    )
