from pathlib import Path
import pandas as pd
from dateutil.parser import parse
from typing import Tuple

W4 = (
    ">>>>>> Begin Section 04: [LOCAL_GEO_WINDS] -- Winds in m/s at the station location, aligned GEOGRAPHICALLY",
    ">>>>>> End Section 4",
)


def plotsav(fn: Path) -> pd.DataFrame:
    """Get what's in IDL .sav file
    https://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.io.readsav.html
    """
    from scipy.io import readsav

    dat = readsav(fn, python_dict=True)

    return dat


def txt2dat(fn: Path) -> pd.DataFrame:
    """convert ASCII to array"""
    fn = Path(fn).expanduser()

    istart, iend = index_lineno(fn, *W4)

    dat = pd.read_csv(
        fn,
        skiprows=istart + 2,
        nrows=iend - istart - 2,
        sep=r"\s+",
        names=["Begin Time", "End Time", "Zonal Wind", "Sigma Zon", "Merid Wind", "Sigma Mer", "Vertical Wind", "Sigma Vz"],
    )

    dat.filename = fn
    # %% put time in native format
    dat["Begin Time"] = [parse(t).time() for t in dat["Begin Time"]]
    dat["End Time"] = [parse(t).time() for t in dat["End Time"]]

    return dat


def index_lineno(fn: Path, start_pat: str, end_pat: str) -> Tuple[int, int]:
    """give index of LINE matching PAT in FILE"""

    with fn.open("r") as f:
        for i, line in enumerate(f):
            if W4[0] in line:
                start_index = i
            if W4[1] in line:
                end_index = i
                break

    return start_index, end_index
