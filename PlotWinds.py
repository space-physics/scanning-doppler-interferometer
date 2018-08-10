#!/usr/bin/env python
"""
Get/Parse Mark Conde's Scanning Doppler Interferometer data, particularly for Winds.

Read text file:

PlotWinds data/PKR_2017_061_date_03_02_sky_5577_nz0115.txt
"""
from pathlib import Path
from matplotlib.pyplot import show
from argparse import ArgumentParser
import scanning_doppler_interferometer as sdi
import scanning_doppler_interferometer.plots as sdiplot


def main():
    p = ArgumentParser()
    p.add_argument('fn')
    p = p.parse_args()

    fn = Path(p.fn).expanduser()

    if fn.suffix == '.sav':
        dat = sdi.plotsav(fn)
    else:
        dat = sdi.txt2dat(fn)
        sdiplot.plotwinds(dat)

    show()


if __name__ == '__main__':
    main()
