#!/usr/bin/env python
"""
Get/Parse Mark Conde's Scanning Doppler Interferometer data, particularly for Winds.

Michael Hirsch, Ph.D.
SciVision, Inc.
"""
from pathlib import Path
from scipy.io import readsav

W4='>>>>>> Begin Section 04: [LOCAL_GEO_WINDS] -- Winds in m/s at the station location, aligned GEOGRAPHICALLY'

fn = 'data/PKR_2017_061_date_03_02_sky_5577_nz0115.txt'

def plotsav(fn):
    """Plot what's in IDL .sav file"""
    dat = readsav(fn, python_dict=True)

    return dat


def index_lineno(fn,pat):
    """give index of LINE matching PAT in FILE"""



if __name__ == '__main__':
    from argparse import ArgumentParser
    p = ArgumentParser()
    p.add_argument('fn')
    p = p.parse_args()

    fn = Path(p.fn).expanduser()
    if fn.suffix=='.sav':
        dat = plotsav(fn)
    else:
        pass