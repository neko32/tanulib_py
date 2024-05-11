import yaml
from csv import writer
from typing import Optional, Any


def to_csv(yaml_file: str, csv_file: str, verbose: bool = False) -> None:
    """Convert from yaml to CSV"""

    with open(csv_file, "w") as w_csv_fd:
        csvw = writer(w_csv_fd)

        with open(yaml_file, "r") as r_yaml_fd:
            root = yaml.safe_load(r_yaml_fd)
            tbl = {}
            headers = ["key"]
            cnt = 0
            for k, v in root.items():
                sub_tbl = {}
                rows = [k]
                _trav(v, sub_tbl, headers, rows)
                tbl[k] = sub_tbl

                if verbose:
                    print(headers)
                    print(rows)

                if cnt == 0:
                    csvw.writerow(headers)
                csvw.writerow(rows)

                cnt += 1

        if verbose:
            print(tbl)


def _trav(
        h: Optional[dict[Any, Any]],
        tbl: dict[Any, Any],
        headers: list[str],
        rows: list[Any],
        parent_name: str = ""):
    for k, v in h.items():
        if isinstance(v, dict):
            _trav(v, tbl, headers, rows, parent_name + k)
        else:
            kv = "_".join([parent_name, k])
            if kv.startswith("_"):
                kv = kv[1:]
            if kv not in headers:
                headers.append(kv)
            tbl[k] = kv
            rows.append(v)
